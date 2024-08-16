
# Quote Generator using Tkinter

This is a simple quote generator application built using Python's `tkinter` library. The application fetches random quotes from an online API and displays them on a graphical user interface.

## Features

- Fetches random quotes from different APIs.
- Displays the quote on a canvas with a background image.
- Uses a button to fetch and display a new quote.


## Screenshots

Here are some screenshots of the application:

![Quote Generator Screenshot 1](start.png)

![Quote Generator Screenshot 2](start2.png)

## APIs Used

Here are some APIs that can be used to fetch random quotes:

1. **ZenQuotes API**
   - **Endpoint:** `https://zenquotes.io/api/random`
   - Provides a random quote each time you make a request.

2. **Quotable API**
   - **Endpoint:** `https://api.quotable.io/random`
   - Provides a random quote along with the author's name.

3. **FavQs API**
   - **Endpoint:** `https://favqs.com/api/qotd`
   - Provides the quote of the day.

## Troubleshooting

If you encounter issues where quotes are not being fetched, here are some potential solutions:

1. **Check Internet Connectivity**
   - Ensure that your internet connection is active and stable.

2. **DNS Resolution**
   - Try using a different DNS server, such as Google's `8.8.8.8`, or flush your DNS cache.
   - On Windows: `ipconfig /flushdns`
   - On macOS/Linux: `sudo dscacheutil -flushcache` or `sudo systemctl restart nscd`

3. **Test API Access**
   - Open a browser and try to access the API endpoint directly to see if it's reachable.

4. **Simple Python Script**
   - Use a minimal Python script to check if the issue persists outside of the Tkinter environment. Example:
     ```python
     import requests as req

     try:
         response = req.get("https://api.quotable.io/random")
         response.raise_for_status()
         data = response.json()
         print(data['content'])
     except req.exceptions.RequestException as e:
         print(f"Failed to retrieve quote: {e}")
     ```

5. **Firewall/Antivirus Software**
   - Temporarily disable any firewall or antivirus software to see if they are blocking outgoing requests.

6. **Use a VPN**
   - If you suspect network restrictions, try using a VPN to bypass them.

7. **Python Version/Library Issues**
   - Ensure you're using an up-to-date version of Python and the `requests` library. Upgrade the `requests` library if necessary:
     ```sh
     pip install --upgrade requests
     ```

## License

This project is licensed under the MIT License.

## Author

- **Umesh Kumar Sahoo**
  - GitHub: [umeshkumarsahoo](https://github.com/umeshkumarsahoo)
