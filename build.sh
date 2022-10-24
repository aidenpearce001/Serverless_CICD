for folder in mongodb_crud/CRUD/* ; do
    zip_name=$(echo $folder | cut -d "/" -f 3)
    zip -j "${zip_name}.zip" "$folder/app.py"
done