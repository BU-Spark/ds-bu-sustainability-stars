from flask import Flask, request, render_template,send_file
import pandas as pd
from io import BytesIO


app = Flask(__name__)

# Load the dataset
data = pd.read_csv('gs_result_notcomplete.csv')
data = data[['uid','Author','Title','Abstract','dep','Year']]
@app.route('/', methods=['GET', 'POST'])
def index():
    # Filtered results start with all data
    filtered_data = data
    
    if request.method == 'POST':
        author = request.form.get('author', '').strip().lower()
        dep = request.form.get('dep', '').strip().lower()
        year=request.form.get('Year','')

        # Filter by author if input provided
        if author:
            filtered_data = filtered_data[filtered_data['Author'].str.lower().str.contains(author)]
        
        if year:
            year = int(year)
            filtered_data = filtered_data[filtered_data['Year']==year]
        
        # Filter by department if input provided and at least 3 characters
        if dep and len(dep) >= 3:
            filtered_data = filtered_data[filtered_data['dep'].str.lower().str.contains(dep)]
    
    # Convert filtered data to HTML
    table = filtered_data.to_html(index=False, classes='table table-bordered', escape=False)
    return render_template('index.html', table=table)

@app.route('/download', methods=['POST'])
def download():
    # Start with all data and apply filters again
    filtered_data = data
    author = request.form.get('author', '').strip().lower()
    dep = request.form.get('dep', '').strip().lower()
    year = request.form.get('Year', '')

    # Apply filters
    if author:
        filtered_data = filtered_data[filtered_data['Author'].str.lower().str.contains(author)]
    
    if year:
        year = int(year)
        filtered_data = filtered_data[filtered_data['Year'] == year]
    
    if dep and len(dep) >= 3:
        filtered_data = filtered_data[filtered_data['dep'].str.lower().str.contains(dep)]
    
    # Convert the entire filtered dataset to CSV
    csv_buffer = BytesIO()
    filtered_data.to_csv(csv_buffer, index=False, encoding='utf-8')  # Encode CSV as UTF-8
    csv_buffer.seek(0)

    # Send file to the user
    return send_file(csv_buffer, mimetype='text/csv', as_attachment=True, download_name='filtered_data.csv')


if __name__ == '__main__':
    app.run(debug=True)
