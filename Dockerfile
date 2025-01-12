FROM --platform=linux/amd64 python:3.12-slim

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy the app into the container
COPY . /app

# set the working directory
WORKDIR /app

# set the environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# install/sync the dependencies
RUN uv sync --frozen --no-cache

# run the app
CMD ["/app/.venv/bin/uvicorn", "policy_wonks.app:api", "--host", "0.0.0.0", "--port", "10000"]
