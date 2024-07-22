#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
SRC_DIR="${SCRIPT_DIR}/src"
PACKAGE_DIR="${SCRIPT_DIR}/package"
DEPLOYMENT_FILENAME="rabbit-manager-lambda_deployment.zip"
DEPLOYMENT_PATH="${SCRIPT_DIR}/${DEPLOYMENT_FILENAME}"

set -e

echo "Cleaning..."
cd "${SRC_DIR}"
rm -rf "${PACKAGE_DIR}"
rm -f "${DEPLOYMENT_PATH}"
echo

# echo "Downloading dependencies..."
# mkdir -p "${PACKAGE_DIR}"
# pip install --target="${PACKAGE_DIR}" package-name
# echo
#
# echo "Packaging dependencies..."
# cd "${PACKAGE_DIR}"
# zip -r "${DEPLOYMENT_PATH}" .
# cd "${SCRIPT_DIR}"

echo "Packaging scripts..."
cd "${SRC_DIR}"
zip -r "${DEPLOYMENT_PATH}" .
cd "${SCRIPT_DIR}"
echo

echo "Done"
