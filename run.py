import loader

if __name__ == '__main__':
	print('[Starting] ...')
	loader.executor.start_polling(loader.dp, skip_updates=True)