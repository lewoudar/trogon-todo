from trogon_todo.console import console


def get_done_argument(done: bool, not_done: bool) -> bool | None:
    if done and not_done:
        console.print('[error]You cannot simultaneously set [bold]--done[/] and [bold]--not-done[/] flags.')
        raise SystemExit(1)

    if not done and not not_done:
        return None
    if done:
        return True
    if not_done:
        return False
