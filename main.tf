resource "aws_instance" "test_server" {
  ami           = "ami-06aa3f7caf3a30282"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleWebAppServer"
  }
}


# Muhammad Mohsin 
