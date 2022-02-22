##### Table of Contents

[AWS Public vs Private Services](#AWS-Public-vs-Private-Services)

[AWS Default Virtual Private Cloud](#AWS-Default-Virtual-Private-Cloud)

[Shared Responsibility Model](#Shared-Responsibility-Model)

[High-Availability vs Fault-Tolerance vs Disaster Recovery](#High-Availability-vs-Fault-Tolerance-vs-Disaster-Recovery)

[IAM Identity Policies](#IAM-Identity-Policies)

[IAM Users and ARNs](#IAM-Users-and-ARNs)

####### AWS Public vs Private Services
  * Private service are the service within the vpc
  * private service access public services or internet via IGW
  * public service is access using public endpoints eg : s3
  * public service is nothing but attached to a public network interface
  
###### AWS Default Virtual Private Cloud
  * A default VPC is created once per region when an AWS account is first created.
  * There can only be one default VPC per region, and they can be deleted and recreated from the console UI .
  * They always have the same IP range and same '1 subnet per AZ' architecture.
  * VPC are private and isolated 
  * Default VPC cidr : 172.31.0.0/16
  * Higher the number in /(20) smaller is the network size in each region
  * internet gateway, Security group and Nacl are pre configured in default vpc
  * By default anything placed or deployed in default vpc are assigned public IPv4 address
  
###### Shared Responsibility Model
  * The Shared Responsibility Model - is how AWS provide clarity around which areas of systems security are theirs, and which are owned by the customer
  * AWS Responsibility for security of cloud : security managed by aws for  regions, AZ, Edge location , hardware/aws global infra , Compute storage, database ,networking, software
  * Customer Responsibility for security of cloud : Customer data , platform , Application, Identity & access management, operating system, network & local firewall ,client-side data encryption, integrity & authentication ,  server-side encryption(file system and or data) , networking traffic protection (Encryption , integrity, identity)
  
###### High-Availability vs Fault-Tolerance vs Disaster Recovery
  * HA : aims to ensure an agreed level of operational performance, usually uptime for a higher than normal period
    * 99.9%(Three 9's ) = 8.77 hours p/year downtime
    * 99.999%(five 9's ) = 5.5 minutes p/year downtime
    * you have spare parts and tools required to replace and minimize disruption
	* minimize the outages
	* mostly like active-passive
  
  * Fault-Tolerance (FT):
    * The property that enables a system to continue operating properly in the event of the failure of some (one or more faults within) of its components
	* mostly like active-active
	* (costly and very complex to implement)
	* Operate through faults
  
  * Disaster Recovery (DR):
    * A set of policies ,tools and procedures to enable the recovery or continuation of vital technolgy infra and systems following a natural or human-induced disaster
	* used when HA and FT don't work

###### IAM Identity Policies:
  * Identity Policies are attached to AWS identities and either ALLOW or DENY access to AWS resources.
  * "sid" - statement to describe about policy
  * action - service:operation , example ["Action" : "S3:*"]
  * resource - matches aws resources, it can be list
  * effect : allow or deny 
  
  * Explicit Deny
  * Explict ALLOW
  * Default Deny
  * IAM USER by default has no access to any aws services
  * we have two types of policy inline(individual policy attached) and managed policy (reusable , low management overhead)

###### IAM Users and ARNs
  * IAM Users are an identity used  for anything requiring long term aws access eg : Humans, Application or service accounts
  * ARN : Uniquely identity resurces within any aws accounts
  * 5000 IAM Users per account
  * IAM user can be member of 10 groups
  * This system has design impacts
    - Internet scale application
	- Large Orgs & org merges
  * IAM Roles and Identity Federation fix the limitation issue

###### 
  
  
