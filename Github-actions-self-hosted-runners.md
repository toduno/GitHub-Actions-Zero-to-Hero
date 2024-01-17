# GitHub Actions Runners -
Runner - a place to run your test/job on. 

Github-hosted runner - runner hosted by Github to run your test/job. It's for public use and general purpose.

Self-hosted runner - a place you specifically set to run your test/job on. E.g using Jenkins, you can install Jenkins and create another EC2 instance or a docker container which will act as a runner. It's private and only you has access. 3 key reasons to use self-hosted runners: security, private repos, don't have a Github hosted runner matching your requirements.

# Practical - Use an ec2 instance to create a self-hosted runner
1. Create a simple ec2 instance that you'll attach to Github for it to communicate with it (e.g. just like how in Jenkins, Jenkins master communicates with Jenkins worker or agent using the ssh protocol).
2. Configure an inbound and outbound rule for Github to access the ec2 instance in and out via https and https network type.
3. Convert your Github-hosted runner to Github self-hosted runner via your CI file i.e the actions file in jobs: build: runs-on: e.g. self-hosted.  Before then, firstly, you can go to settings - actions - runners - new self-hosted runner and ensure you provide the correct details e.g. if it's an ubuntu server in the ec2 instance, select Linux for runner image, your system's architecture (since the ec2 is a virtual machine that still uses your system's architecture), then connect to the ec2 (via ssh, instance connect etc) to download the runner package and validate its hash (with Githb tokens) after which you can create the runner and start the configuration experience and run it to configure the ec2 as a runner and connect your Github to it. And finally use the yaml in your workflow file for each job - runs-on: self-hosted. 

Now you have your own self-hosted place to run your test on