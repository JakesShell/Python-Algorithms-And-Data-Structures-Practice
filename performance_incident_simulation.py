import random
import time

def build_user_records(total_users):
    records = []

    for index in range(total_users):
        records.append({
            "user_id": f"user-{index:05d}",
            "plan": "business" if index % 5 == 0 else "standard",
            "region": "us-east-1" if index % 2 == 0 else "eu-west-1"
        })

    return records


def build_request_load(total_requests, total_users):
    random.seed(42)
    requests = []

    for _ in range(total_requests):
        user_number = random.randint(0, total_users - 1)
        requests.append(f"user-{user_number:05d}")

    return requests


def baseline_linear_lookup(user_records, request_load):
    matched_requests = 0

    for requested_user_id in request_load:
        for record in user_records:
            if record["user_id"] == requested_user_id:
                matched_requests += 1
                break

    return matched_requests


def optimized_index_lookup(user_records, request_load):
    indexed_records = {record["user_id"]: record for record in user_records}
    matched_requests = 0

    for requested_user_id in request_load:
        if requested_user_id in indexed_records:
            matched_requests += 1

    return matched_requests


def measure_execution_time(label, operation):
    start_time = time.perf_counter()
    result = operation()
    end_time = time.perf_counter()
    elapsed_seconds = end_time - start_time

    return {
        "label": label,
        "result": result,
        "elapsed_seconds": elapsed_seconds
    }


def calculate_improvement_percentage(baseline_seconds, optimized_seconds):
    if baseline_seconds == 0:
        return 0

    return ((baseline_seconds - optimized_seconds) / baseline_seconds) * 100


def print_report(baseline_result, optimized_result, total_users, total_requests):
    improvement = calculate_improvement_percentage(
        baseline_result["elapsed_seconds"],
        optimized_result["elapsed_seconds"]
    )

    print("Cloud Application Performance Incident And Optimization")
    print("=" * 62)
    print("Incident: Users reported slow response times during peak usage.")
    print("Environment: Simulated cloud-hosted application backend")
    print(f"Simulated Users: {total_users}")
    print(f"Simulated Requests: {total_requests}")
    print("")
    print("Investigation Summary")
    print("-" * 62)
    print("Suspected Bottleneck: Repeated user record lookup under load")
    print("Baseline Approach: Linear search through user records")
    print("Optimized Approach: Dictionary-based indexed lookup")
    print("")
    print("Benchmark Results")
    print("-" * 62)
    print(f"Baseline Matched Requests: {baseline_result["result"]}")
    print(f"Baseline Execution Time: {baseline_result["elapsed_seconds"]:.6f} seconds")
    print(f"Optimized Matched Requests: {optimized_result["result"]}")
    print(f"Optimized Execution Time: {optimized_result["elapsed_seconds"]:.6f} seconds")
    print(f"Estimated Improvement: {improvement:.2f}%")
    print("")
    print("Resolution")
    print("-" * 62)
    print("Refactored repeated linear lookup into indexed dictionary lookup.")
    print("This reduces repeated search cost and improves response behavior under simulated load.")
    print("")
    print("Operational Outcome")
    print("-" * 62)
    print("Performance degradation was reproduced, measured, optimized, and validated.")
    print("This mirrors a cloud support workflow for diagnosing backend performance incidents.")


def main():
    total_users = 4000
    total_requests = 18000

    user_records = build_user_records(total_users)
    request_load = build_request_load(total_requests, total_users)

    baseline_result = measure_execution_time(
        "Baseline Linear Lookup",
        lambda: baseline_linear_lookup(user_records, request_load)
    )

    optimized_result = measure_execution_time(
        "Optimized Indexed Lookup",
        lambda: optimized_index_lookup(user_records, request_load)
    )

    print_report(baseline_result, optimized_result, total_users, total_requests)


if __name__ == "__main__":
    main()

