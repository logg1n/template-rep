def func_name(arguments: dict):
    from typing import Any, Dict

    # --- Типы (Type Aliases) ---
    ErrorResponse = Dict[str, Any]
    SuccessResponse = Dict[str, Any]

    def error_response(error: str, details: str) -> ErrorResponse:
        """Возвращает унифицированную структуру ошибки."""
        return {"status": "error", "result": {"error": error, "details": details}}

    def success_response(data: Any) -> SuccessResponse:
        """Возвращает унифицированную структуру успеха."""
        return {"status": "success", "result": {"data": data, "success": True}}

    debug: bool = arguments.get("debug", False)

    if debug:
        print(f"DEBUG: Start function {__name__}")
        print(f"DEBUG: Args: {arguments}")

    try:
        # imports packages

        return success_response("Success")

    except Exception as e:
        if debug:
            import traceback

            traceback.print_exc()
        return error_response(str(type(e).__name__), str(e))
