from fastapi import APIRouter

router = APIRouter()


# --- Module 1 (APIs) ---
# This endpoint is intentionally broken. It accepts ANY JSON payload,
# with no validation on structure, source, or content, and immediately
# acts on whatever "dosage_instruction" it finds.
#
# This mirrors the real Doctronic incident: a fabricated regulatory
# bulletin was accepted and acted on without question.
#
# DO NOT fix this in Module 1. You'll add validation in Module 2.

@router.post("/bulletin")
def receive_bulletin(bulletin: dict):
    dosage_note = bulletin.get("dosage_instruction", "")
    return {
        "status": "accepted",
        "action": f"Applying instruction: {dosage_note}",
    }
