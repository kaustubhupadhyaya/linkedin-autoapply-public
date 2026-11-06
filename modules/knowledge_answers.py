"""Per-tool years and AI grounding, loaded from an optional private knowledge module.

Set CANDIDATE_KNOWLEDGE_MODULE to the path of a module that exposes
years_answer(), format_years(), log_gap(), named_object(), prompt_block() and
resume_block(). When the variable is unset or the module cannot be loaded, every
function returns what the bot would have done without it. Nothing here raises
into the bot.
"""
import importlib.util
import os
import threading

KNOWLEDGE_MODULE = os.environ.get("CANDIDATE_KNOWLEDGE_MODULE", "")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAP_LOG = os.path.join(REPO, "logs", "knowledge_gaps.jsonl")

_K = None
_tried = False
_lock = threading.Lock()


def _knowledge():
    """The configured knowledge module, loaded once; None when it cannot be loaded."""
    global _K, _tried
    with _lock:
        if not _tried:
            _tried = True
            if not KNOWLEDGE_MODULE or not os.path.exists(KNOWLEDGE_MODULE):
                _K = None
                return None
            try:
                spec = importlib.util.spec_from_file_location("portal_knowledge", KNOWLEDGE_MODULE)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                _K = mod
            except Exception as e:
                print(f"knowledge file module not usable ({type(e).__name__}: {str(e)[:100]}); the bot's own answers stand.", flush=True)
                _K = None
    return _K


def knowledge_years(label: str, default):
    """A text field asking for years (or months) of experience. With a tool named that the knowledge file has a number for, that number
    (whole years, or whole months when the label asks for months); otherwise `default`, the answer the bot would have typed anyway.
    A tool named without a number is written to logs/knowledge_gaps.jsonl so the number can be supplied."""
    K = _knowledge()
    if K is None:
        return default
    try:
        kind, years, skills = K.years_answer(label)
        if kind == "known":
            return K.format_years(years, label)
        if kind == "unknown":
            K.log_gap(GAP_LOG, label, "years_unknown", skills, "no number for these tools in candidate_knowledge.json; the bot's default was typed")
        elif kind == "none":
            obj = K.named_object(label)
            if obj:
                K.log_gap(GAP_LOG, label, "years_no_key", [obj], "a tool the knowledge file does not list at all; the bot's default was typed")
    except Exception:
        pass
    return default


def grounding_text() -> str:
    """The text an LLM may use to answer about the candidate: the verified facts with the per-tool years, then the resume lines. Empty string
    when the knowledge file cannot be read (the caller then has nothing to ground an answer on and must not ask the model)."""
    K = _knowledge()
    if K is None:
        return ""
    try:
        facts = K.prompt_block()
        if not facts:
            return ""
        resume = K.resume_block()
        return facts + ("\n\n" + resume if resume else "")
    except Exception:
        return ""
