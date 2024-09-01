FROM python:3.12-slim
COPY calculator.py calculator_helper.py requirements.txt calculator_rest_service.py logger.py models.py /
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "calculator.py"]
