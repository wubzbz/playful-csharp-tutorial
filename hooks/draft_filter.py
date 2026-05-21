"""MkDocs hook: 过滤 draft: true 的页面。"""
from __future__ import annotations

import logging

log = logging.getLogger("mkdocs.hooks.draft_filter")


def on_files(files, **kwargs):
    """移除 front matter 中标记 draft: true 的文件。"""
    kept = []
    removed = 0
    for f in files:
        if _is_draft(f):
            removed += 1
        else:
            kept.append(f)

    if removed:
        log.info(f"已排除 {removed} 个草稿页面")
    return type(files)(kept)


def _is_draft(file) -> bool:
    src = getattr(file, "content_bytes", None)
    if not src:
        if hasattr(file, "abs_src_path"):
            try:
                with open(file.abs_src_path, encoding="utf-8") as fh:
                    src = fh.read().encode("utf-8")
            except Exception:
                return False
        else:
            return False

    text = src.decode("utf-8", errors="ignore")
    if not text.startswith("---"):
        return False

    parts = text.split("---", 2)
    if len(parts) < 2:
        return False

    fm_text = parts[1].strip()
    if not fm_text:
        return False

    for line in fm_text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            continue
        if line in ("draft: true", "draft:true", "draft: True", "draft:True"):
            return True
        if line.startswith("draft:") and "true" in line.lower():
            val = line.split(":", 1)[1].strip().lower()
            if val.startswith("true"):
                return True

    return False
