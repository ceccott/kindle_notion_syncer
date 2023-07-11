# Base image
FROM python:3

# Install Google Chrome
RUN apt-get update && \
    apt-get install -y wget gnupg2 cron && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN apt-get install -yqq unzip && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Set display environment variable (optional, may be needed for headless operation)
ENV DISPLAY=:99

# Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clone repo
RUN git clone https://github.com/ceccott/kindle_notion_syncer.git /app

# Set the working directory
WORKDIR /app

# Add cron job to crontab
RUN echo "0 0 * * * python /app/kindle_notion_syncer.py >> /var/log/cron.log 2>&1" >> /etc/crontab

# Create the log file
RUN touch /var/log/cron.log

# Run cron and your application
CMD cron && tail -f /var/log/cron.log
