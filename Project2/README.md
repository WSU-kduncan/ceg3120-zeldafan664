# Project 2 Rubric

/ 15

## Part 1 ( / 5)


1. VPC created & configured & role described
    -The role of the VPC is to build a virtual network in the AWS cloud, without any VPN's or hardware required. 
    
2. Subnet created & configured & role described
    -A subnet is a range of IP addresses in your VPC. You can attach AWS resources, such as EC2 instances into a user-specified subnet. 
3. Internet gateway created & configured & role described
    -An internet gateway provides a target in your VPC route tables for internet-routable traffic. For communication using IPv4, the internet gateway also      performs network address translation (NAT).
4. Route table created and configured & role described
    -The rold of the route table is to control where network traffic is directed. Each subnet in your VPC must be associated with a route table, which controls the routing for the subnet (subnet route table). You can explicitly associate a subnet with a particular route table.
5. Security group created and configured & role described
    -A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance. When you create a VPC, it comes with a default security group.

## Part 2 ( / 10)

1. Instance details
   - AMI selected: Ubuntu
   - default username of the instance type selected
        ubuntu

   - Instance type selected: t2.micro
2. How to attach instance to VPC
    -After selecting "Launch Instance", edit the network settings and select your previously created VPC from the dropdown menu. 
3. Public IP address auto-assign - yay or nay and why?
    -Gonna be a no from me dawg. I'd rather manually assign the IP.
4. How to create and attach storage volume to instance
    -On the configure storage menu, just select how many GiB of storage you would like and of what type. (I stuck with 8 GiB og gp2).
5. How to tag instance with "Name" of "YOURLASTNAME-instance"
    Under Tags, set the Key to Name and the value to "YOURLASTNAME-Instance
6. How to associate VPC security group (your security group) with your instance
    -On the security tab, just select the previously created security group that is associated with the same VPC created.
7. How to create / reserve and associate and Elastic IP address with your instance
    -First, on the left panel, scroll down and select Elastic IPs
    -Select Allocate Elastic IP address
    -Select from Amazon pool of IPV4 addresses in the region that you want (Us-east)
    -Add a tag with the Key being Name and the value being "LASTNAME-EIP"
8. Screenshot with instance details: (In images folder)
9. How to change hostname via commands on instance
    -Edit the ssh config file like so: 
    Host aws
        HostName 34.225.33.244
        user ubuntu
        IdentityFile /home/liam/ceg3120key.pem
~

10. Screenshot of successful SSH connection to instance (with your new hostname instead of ip-##-##-##-##)
    -The connection keeps timing out :(
## Point Deductions ( / 1)

- images not included in markdown documentation
