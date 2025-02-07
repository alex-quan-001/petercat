import json
from fastapi import APIRouter
from insight.service.activity import get_active_dates_and_times, get_activity_data
from insight.service.issue import get_issue_data
from insight.service.pr import get_code_frequency, get_pr_data


# ref: https://open-digger.cn/en/docs/user_docs/metrics/metrics_usage_guide
router = APIRouter(
    prefix="/api/insight",
    tags=["insight"],
    responses={404: {"description": "Not found"}},
)


@router.get("/issue")
def get_issue_insight(repo_name: str):
    try:
        result = get_issue_data(repo_name)
        return {
            "success": True,
            "data": result,
        }

    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})


@router.get("/pr")
def get_pr_insight(repo_name: str):
    try:
        result = get_pr_data(repo_name)
        return {
            "success": True,
            "data": result,
        }

    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})


@router.get("/code_frequency")
def get_code_frequency_insight(repo_name: str):
    try:
        result = get_code_frequency(repo_name)
        return {
            "success": True,
            "data": result,
        }

    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})


@router.get("/activity")
def get_activity_insight(repo_name: str):
    try:
        result = get_activity_data(repo_name)
        return {
            "success": True,
            "data": result,
        }

    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})


@router.get("/active_dates_and_times")
def get_active_dates_and_times_insight(repo_name: str):
    try:
        result = get_active_dates_and_times(repo_name)
        return {
            "success": True,
            "data": result,
        }

    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})
