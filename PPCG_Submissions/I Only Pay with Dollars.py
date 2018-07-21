# This Challenge: http://codegolf.stackexchange.com/questions/83756/i-only-pay-with-dollars/83768#83768
Y=lambda u:'${:,.2f}'.format(float(u[1:].translate([{44:''},{44:46,46:''}]['€'in u]))*{'€':1.1,'£':1.37,'¥':.15}[u[0]])

print(Y('€2.121,37'))