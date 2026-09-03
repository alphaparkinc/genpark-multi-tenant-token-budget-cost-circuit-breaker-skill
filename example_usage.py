from client import MultiTenantTokenBudgetCostCircuitBreakerClient

def main():
    client = MultiTenantTokenBudgetCostCircuitBreakerClient()
    res = client.enforce_tenant_spend_limit('tnt_startup_8812', 2048, 100.0, 99.5)
    print('Multi-Tenant FinOps Circuit Breaker: ' + res['finops_circuit_id'] + ' (' + res['tenant_id'] + ')')
    print('Allowed: ' + str(res['allow_request_execution']) + ' | Utilization: ' + str(res['budget_utilization_pct']) + '%')
    print('Dossier URL: ' + res['finops_telemetry_dossier_url'])

if __name__ == '__main__':
    main()
