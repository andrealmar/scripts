#  /webtools/oracle/plat1200_1/middleware/oracle_common/common/bin/wlst.sh weblogic_add_users.py

# Author: ANDRE ALMAR

servidor = raw_input('Digite o servidor: ')
porta = raw_input('Digite a porta: ')
usuario = raw_input('Digite o usuario: ')
password = raw_input('Digite o password: ')
roles = ['Deployer', 'Monitor', 'Operator', 'IntegrationDeployer', 'IntegrationMonitor', 'IntegrationOperator']

connect(usuario,password,'t3://' + servidor + ':' + porta )

serverConfig()

cd('/SecurityConfiguration/'+domainName+'/Realms/myrealm/RoleMappers/XACMLRoleMapper')

f = open('users.csv')

for line in f.readlines():
  items = line.split(',')
  for role in roles:
    try:
      expr = cmo.getRoleExpression('', role)
      print 'Usr(' + line + ') was assigned to role ' + role
      cmo.setRoleExpression('', role, 'Usr(' + line + ') | '  + expr)
    except:
      print "Role " + role +  " doesn't exist"

exit()