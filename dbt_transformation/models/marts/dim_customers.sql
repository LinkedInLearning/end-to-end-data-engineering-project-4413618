with
    customers as (select * from {{ ref("stg_customers") }}),
    orders as (select * from {{ ref("stg_orders") }}),
    customer_orders as (
        select
            c.customer_id,
            c.email,
            c.country,
            c.city,
            min(o.order_approved_at) as first_order_date,
            max(o.order_approved_at) as most_recent_order_date,
            count(o.order_id) as number_of_orders
        from orders o
        inner join customers c using (customer_id)
        group by c.customer_id, c.email, c.country, c.city
    )
select *
from customer_orders
