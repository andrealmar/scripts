servidor = raw_input('Digite o servidor: ')
porta = raw_input('Digite a porta: ')
usuario = raw_input('Digite o usuario: ')
password = raw_input('Digite o password: ')

connect(usuario,password,'t3://' + servidor + ':' + porta )

serverConfig()

cd('/SecurityConfiguration/'+domainName+'/Realms/myrealm/RoleMappers/XACMLRoleMapper')

expr = cmo.getRoleExpression('','Deployer')

cmo.setRoleExpression('', 'Deployer', 'Usr(OI273541, TR111111, TR2222221, TR333333) | Usr(TR483945, TR483944) | Usr(deployer_devops) | ' + expr)


# ./oracle/plat1200/middleware/wlserver/common/bin/wlst.sh
# 'Deployer', 'Usr(TR394655, TR026695, TR035299, TR592925, TR095869, TR417375, TR059823)

# Integration Monitor
# Integration Deployer
# Integration Operator
# Monitor 
# Deployer
# Operator