BACKEND_DIR = .
FRONTEND_DIR = app/frontend
TYPES_FILE = $(FRONTEND_DIR)/src/types/types.ts
OPENAPI_SCHEMA = openapi.json

.PHONY: help backend frontend types install run clean test

help:
	@echo "Available commands:"
	@echo "  make install     - Install all dependencies (backend + frontend)"
	@echo "  make backend     - Run the FastAPI backend"
	@echo "  make frontend    - Start the React frontend (with type updates)"
	@echo "  make types       - Generate TypeScript types from OpenAPI schema"
	@echo "  make run         - Run both backend and frontend concurrently"
	@echo "  make test        - Run frontend tests with Vitest"
	@echo "  make clean       - Clean up build artifacts"

install:
	@echo "Installing backend dependencies..."
	cd $(BACKEND_DIR) && python3 -m venv venv && venv/bin/pip install -r requirements.txt
	@echo "Installing frontend dependencies..."
	cd $(FRONTEND_DIR) && npm install

backend:
	@echo "Starting the FastAPI backend..."
	cd $(BACKEND_DIR) && venv/bin/uvicorn app.main:create_app --reload

types:
	@echo "Generating TypeScript types from OpenAPI schema..."
	# Ensure backend is running to fetch the OpenAPI schema
	cd $(BACKEND_DIR) && venv/bin/uvicorn app.main:create_app --port 8000 &
	sleep 5  # Allow server to start
	curl -s http://127.0.0.1:8000/openapi.json -o $(BACKEND_DIR)/$(OPENAPI_SCHEMA)
	npx openapi-typescript $(BACKEND_DIR)/$(OPENAPI_SCHEMA) -o $(TYPES_FILE)
	pkill uvicorn
	@echo "TypeScript types updated: $(TYPES_FILE)"

frontend:
	@echo "Starting the React frontend..."
	cd $(FRONTEND_DIR) && npm run dev

test:
	@echo "Running frontend tests with Vitest..."
	pytest $(BACKEND_DIR)/tests
	cd $(FRONTEND_DIR) && npx vitest run --coverage

run: types
	@echo "Starting backend and frontend concurrently..."
	# Start backend in the background
	cd $(BACKEND_DIR) && venv/bin/uvicorn app.main:create_app --reload &
	# Start frontend
	cd $(FRONTEND_DIR) && npm run dev

clean:
	@echo "Cleaning up generated files..."
	rm -f $(BACKEND_DIR)/$(OPENAPI_SCHEMA)
	rm -f $(TYPES_FILE)
