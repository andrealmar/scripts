servidor = raw_input('Digite o servidor: ')
porta = raw_input('Digite a porta: ')
usuario = raw_input('Digite o usuario: ')
password = raw_input('Digite o password: ')


connect(usuario,password,'t3://' + servidor + ':' + porta )
serverConfig()
cd('/SecurityConfiguration/'+domainName+'/Realms/myrealm/RoleMappers/XACMLRoleMapper')

expr = cmo.getRoleExpression('','Deployer')
cmo.setRoleExpression('','Deployer','Usr(OI273541)|' + expr)

expr = cmo.getRoleExpression('','IntegrationDeployer')
cmo.setRoleExpression('','IntegrationDeployer','Usr(OI273541)|' + expr)

expr = cmo.getRoleExpression('','IntegrationMonitor')
cmo.setRoleExpression('','IntegrationMonitor','Usr(OI273541)|' + expr)

expr = cmo.getRoleExpression('','IntegrationOperator')
cmo.setRoleExpression('','IntegrationOperator','Usr(OI273541)|' + expr)

expr = cmo.getRoleExpression('','Monitor')
cmo.setRoleExpression('','Monitor','Usr(OI273541)|' + expr)

expr = cmo.getRoleExpression('','Operator')
cmo.setRoleExpression('','Operator','Usr(OI273541)|' + expr)

print ('Usuarios criados no dominio ' + domainName)

disconnect()
