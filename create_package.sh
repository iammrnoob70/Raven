#!/bin/bash
# Raven Assistant - Package Creator
# This script packages all files for distribution

echo "================================================"
echo "   RAVEN ASSISTANT - PACKAGE BUILDER"
echo "================================================"
echo ""

# Create distribution folder
DIST_FOLDER="RavenAssistant_Package"
mkdir -p "$DIST_FOLDER"
mkdir -p "$DIST_FOLDER/raven_assets"

echo "Copying core files..."
cp raven_assistant.py "$DIST_FOLDER/"
cp raven_requirements.txt "$DIST_FOLDER/"
cp check_setup.py "$DIST_FOLDER/"

echo "Copying documentation..."
cp MAIN_README.md "$DIST_FOLDER/"
cp RAVEN_README.md "$DIST_FOLDER/"
cp SETUP_GUIDE.md "$DIST_FOLDER/"
cp ASSET_GUIDE.md "$DIST_FOLDER/"
cp DOWNLOAD_INSTRUCTIONS.md "$DIST_FOLDER/"

echo "Copying scripts..."
cp setup_raven.bat "$DIST_FOLDER/"
cp start_raven.bat "$DIST_FOLDER/"

echo "Copying character assets..."
cp raven_assets/*.png "$DIST_FOLDER/raven_assets/"

echo ""
echo "================================================"
echo "   PACKAGE CREATED SUCCESSFULLY!"
echo "================================================"
echo ""
echo "Distribution folder: $DIST_FOLDER"
echo ""
echo "Contents:"
ls -lh "$DIST_FOLDER"
echo ""
echo "Assets:"
ls -lh "$DIST_FOLDER/raven_assets"
echo ""
echo "================================================"
echo "   READY FOR DISTRIBUTION"
echo "================================================"
echo ""
echo "You can now:"
echo "1. Zip the '$DIST_FOLDER' folder"
echo "2. Share it with others"
echo "3. Or copy to your Windows PC and run setup_raven.bat"
echo ""
