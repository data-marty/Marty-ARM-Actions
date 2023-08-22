targetScope = 'subscription'

@description('Enter the location to deploy the resource to')
param location string = 'Australia East'

@description('Enter the name for the resource group')
param resourceGroupName string = 'data-marty'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2019-10-01' = {
  name: resourceGroupName
  location: location
  tags: {}
  dependsOn: []
}