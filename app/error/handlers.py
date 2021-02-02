from app.error import bp
from flask import render_template


@bp.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@bp.errorhandler(500)
def internal_server_error(error):
	return render_template('500.html'), 500