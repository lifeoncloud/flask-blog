from flask import Flask, render_template, url_for

app = Flask(__name__)

# Example blog posts data (in-memory list)
posts = [
    {
        'id': 1,
        'title': '첫 번째 블로그 글',
        'content': '이것은 첫 번째 글의 내용입니다.',
        'author': '김철수',
        'date': '2023-01-01'
    },
    {
        'id': 2,
        'title': '두 번째 블로그 글',
        'content': '이것은 두 번째 글의 내용입니다. 좀 더 긴 내용이 들어갈 수 있습니다.',
        'author': '이영희',
        'date': '2023-01-15'
    }
]


@app.route('/')
def index():
    # Render the index.html template, passing the posts data
    return render_template('index.html', title='홈', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    # Find the post with the given id
    # In a real app, this would query a database
    single_post = next((post for post in posts if post['id'] == post_id), None)

    if single_post is None:
        # Handle case where post ID is not found (e.g., render a 404 page)
        return render_template('404.html', title='글을 찾을 수 없음'), 404 # Example: Basic 404

    return render_template('post.html', title=single_post['title'], post=single_post)


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
