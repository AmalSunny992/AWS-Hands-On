# Hands On : Using Amazon LightSail Launch a website with Load Balancer

Setting up two web servers, connecting them to a load balancer on Amazon Lightsail, and pointing them to a domain involves several steps. 
Here's a detailed guide to help you through the process:

## 1. Set Up Two Web Servers on Amazon Lightsail

**Step 1**: Create Two Lightsail Instances

1. Log in to your AWS Management Console.
2. Navigate to Lightsail.
3. Create an instance:

   * Choose the region where you want your instance to be located.
    
   * Select a blueprint (OS or application). For a web server, you can choose Linux/Unix and then select the appropriate app or stack (Here Wordpress is used ).
    
   * Choose an instance plan based on your needs.
    
   * Name your instance (e.g., webserver-1).
    
   * Create the instance.

      **Screenshots** :
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/00c862c6-1a8c-49e4-a35f-8505aeab8967)
      
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/edcc3327-98e1-415f-86b5-31ec2a691324)
      
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/9557eaa8-e0be-499c-a263-1717e230e9b3)      

5. Repeat the process for the second instance (e.g., webserver-2).

**Step 2**: Configure Your Web Servers:
    
    * Connect to each instance via SSH from the Lightsail console.
    
    * Set up your web server (wordpress) and deploy your application or website on both instances. Ensure both servers serve the same content.
  
## 2. Set Up a Load Balancer on Lightsail

**Step 1**: Create a Load Balancer

1. In the Lightsail console, go to the Networking tab.
2. Create a load balancer:
    
    * Name your load balancer (e.g., my-load-balancer).
    
    * Choose the region where your instances are located.
    
    * Create the load balancer.

      **Screenshots** :
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/0505ac29-6d81-4f70-a245-e30265512ff0)
      
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/3ef03fd1-80b1-4058-9364-6a2721a55d75)


**Step 2**: Attach Instances to the Load Balancer

1. After the load balancer is created, go to its management page.
2. Attach your instances (webserver-1 and webserver-2) to the load balancer.

   **Screenshots**:
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/4f5e17e6-b562-4a63-9615-5796adfab3c5)


## 3. Configure SSL/TLS Certificate for the Load Balancer

**Step 1**: Request an SSL/TLS Certificate
1. In the Lightsail console, navigate to your load balancer's management page.
2. Click on the "Certificates" tab.
3. Request a new certificate:
    
    * Enter your domain name.
    
    * Add any additional domain names if needed (e.g., www.yourdomain.com).

      **Screenshots**:
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/aa58073f-3f0a-4371-8c5c-424d133aa428)
      
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/5f1d4a2f-083c-43af-8e23-81fee22c53ff)

**Step 2**: Validate the Domain
1. Follow the instructions to validate your domain. This typically involves adding a CNAME record to your domain's DNS settings.
2. Log in to your domain registrar's account and navigate to the DNS settings.
3. Add the CNAME record provided by Lightsail to your DNS settings.
4. Wait for the validation to complete. This may take some time depending on your DNS provider.

**Step 3**: Attach the Certificate to the Load Balancer
1. Once the certificate is issued, return to the load balancer's management page.
2. In the "Certificates" tab, select the issued certificate and attach it to the load balancer.

   **Screenshot**:
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/4b20a559-964d-45d8-813f-9fcc51ef7225)


## 4. Point Your Domain to the Load Balancer

**Step 1**: Get the DNS Name of the Load Balancer
1. In the Lightsail console, navigate to your load balancer's management page.
2. Copy the DNS name of the load balancer.

**Step 2**: Update Your Domain's DNS Settings Using Amazon Lightsail's Domains and DNS Service
1. Navigate to the Networking tab in the Lightsail console.
2. Click on "Create DNS zone".
3. Enter your domain name and click "Create DNS zone".

   **Screenshots**:
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/47260df8-3d68-4944-bc55-75a15132d869)

4. Add an A record to point your domain to the Lightsail load balancer:

  * In the "DNS zone" management page, click on "Add record".
   
  * Record type: Select "A".
   
  * Subdomain: Leave it blank (or enter @).
   
  * Resolves to: Paste the DNS name of your Lightsail load balancer.
   
  * TTL: Set an appropriate value (e.g., 300 seconds).
   
  * Click "Save".

   **Screenshots**:
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/8b16ae49-ef48-4c27-9792-96cf29d6b2a3)

   
5. Update your domain registrar's nameservers to use Lightsail's nameservers:

  * Log in to your domain registrar's account (e.g., GoDaddy, Namecheap).
   
  * Find the DNS or Nameserver settings for your domain.
   
  * Replace the current nameservers with the ones provided by Lightsail. You can find these in the "DNS zone" management page under "Nameservers".
   
  * Save the changes.

   Screenshots:
      ![image](https://github.com/AmalSunny992/AWS/assets/169422802/f1e03da5-d89e-4fb2-84f3-8504892e7a13)


## 5. Test Your Setup
1. Wait for DNS propagation (this can take a few minutes to 48 hours).
2. Open your web browser and navigate to your domain.
3. Verify that your website is accessible and that the load balancer is distributing traffic between your two instances.
4. Ensure the site is accessible over HTTPS and that the SSL certificate is properly configured

   Final Result ScreenShots (Wordpress Webserver):
   
   **https://www.amasun.in** : 
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/11b00240-b308-470c-8070-f5aa4b3bbf0c)

   **https://info.amasun.in**:
   ![image](https://github.com/AmalSunny992/AWS/assets/169422802/0309b91d-e7f8-4296-bd70-1688ff195344)

    
   
