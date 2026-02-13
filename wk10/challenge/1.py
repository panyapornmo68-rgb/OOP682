class ILogSource:
    def get_logs(self):
        pass

class FileLogSource(ILogSource):
    def get_logs(self):
        return ["Log from Original File"]

class CsvLogSource(ILogSource):
    def get_logs(self):
        print("Reading data from CSV file...")
        return ["Log 1 from CSV", "Log 2 from CSV"]
    
class LogSourceFactory:
    @staticmethod
    def create_source(source_type):
        if source_type == "file":
            return FileLogSource()
        elif source_type == "csv":
            return CsvLogSource()
        raise ValueError("Unknown source type")

source = LogSourceFactory.create_source("csv")


logs = source.get_logs()

for log in logs:
    print(f"แสดงผลบน UI: {log}")