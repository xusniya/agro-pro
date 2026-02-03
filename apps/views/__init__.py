from apps.views.user import (
    UserListAPIView as UserListAPIView,
    UserCreateAPIView as UserCreateAPIView,
    DetailUserAPIView as DetailUserAPIView,
    UpdateUserAPIView as UpdateUserAPIView,
    DeleteUserAPIView as DeleteUserAPIView,
)

from apps.views.farmer import (
    FarmerListAPIView as FarmerListAPIView,
    FarmerCreateAPIView as FarmerCreateAPIView,
    DetailFarmerAPIView as DetailFarmerAPIView,
    UpdateFarmerAPIView as UpdateFarmerAPIView,
    DeleteFarmerAPIView as DeleteFarmerAPIView,
)

from apps.views.buyer import (
    BuyerListAPIView as BuyerListAPIView,
    BuyerCreateAPIView as BuyerCreateAPIView,
    DetailBuyerAPIView as DetailBuyerAPIView,
    UpdateBuyerAPIView as UpdateBuyerAPIView,
    DeleteBuyerAPIView as DeleteBuyerAPIView,
)

from apps.views.distributor import (
    DistributorListAPIView as DistributorListAPIView,
    DistributorCreateAPIView as DistributorCreateAPIView,
    DetailDistributorAPIView as DetailDistributorAPIView,
    UpdateDistributorAPIView as UpdateDistributorAPIView,
    DeleteDistributorAPIView as DeleteDistributorAPIView,
)

from apps.views.supplier import (
    SupplierListAPIView as SupplierListAPIView,
    SupplierCreateAPIView as SupplierCreateAPIView,
    DetailSupplierAPIView as DetailSupplierAPIView,
    UpdateSupplierAPIView as UpdateSupplierAPIView,
    DeleteSupplierAPIView as DeleteSupplierAPIView,
)

from apps.views.health import health as health
