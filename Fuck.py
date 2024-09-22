import requests

# Function to fetch GitHub repositories for a user
def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching repositories.")
        return []

# Main function
def main():
    username = input("Enter GitHub username: ")
    repos = fetch_repositories(username)

    if repos:
        print(f"\nRepositories for {username}:\n")
        for repo in repos:
            print(f"- {repo['name']}: {repo['html_url']}")

if __name__ == "__main__":
    main()
  
