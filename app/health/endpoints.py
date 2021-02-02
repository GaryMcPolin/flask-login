from app.health import bp


@bp.route('/health', methods=['GET'])
def health_check():
	return 'OK', 200
