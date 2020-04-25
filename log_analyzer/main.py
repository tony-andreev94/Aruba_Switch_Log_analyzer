from log_analyzer import file_loader
from log_analyzer import file_handler
from log_analyzer import analyzer

if __name__ == '__main__':
    loaded_logs = file_loader.FileLoader().load_file()
    file_handler_instance = file_handler.FileHandler(loaded_logs)
    formatted_logs = file_handler_instance.format_logs()
    analyze_instance = analyzer.Analyzer(formatted_logs)
    analyzed_result = analyze_instance.analyze()
    analyzed_result.print_results()
