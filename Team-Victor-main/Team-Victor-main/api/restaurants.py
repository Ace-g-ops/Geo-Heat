<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, Query
from typing import List
import logging
from models.schemas import LocationRequest, DensityResponse
from services.google_place import GooglePlacesService
from services.density_calc import calculate_restaurant_density

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter()
places_service = GooglePlacesService()

@router.post("/density-analysis", response_model=DensityResponse)
def analyze_restaurant_density(request: LocationRequest) -> DensityResponse:
    """
    Analyze restaurant density in a given area.
    """
    try:
        logger.info(f"Starting density analysis for lat={request.lat}, lng={request.lng}, radius={request.radius}")
        
        # Get restaurant data
        restaurants = places_service.get_restaurants(request.lat, request.lng, request.radius)
        logger.debug(f"Found {len(restaurants)} restaurants from Google Places API")
        
        # Calculate density
        density_score = calculate_restaurant_density(restaurants, request.radius)
        logger.debug(f"Calculated density score: {density_score}")
        
        # Generate insights
        insights = generate_restaurant_insights(restaurants, density_score)
        
        logger.info(f"Density analysis complete - Score: {density_score}, Restaurants: {len(restaurants)}")
        
        return DensityResponse(
            density_score=density_score,
            business_count=len(restaurants),
            businesses=restaurants,
            insights=insights
        )
        
    except Exception as e:
        logger.error(f"Error in density analysis: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

def generate_restaurant_insights(restaurants, density_score):
    """Generate insights based on restaurant data and density score."""
    logger.debug(f"Generating insights for {len(restaurants)} restaurants with density {density_score}")
    
    insights = []
    
    if density_score < 0.3:
        insights.append("Low restaurant density detected - potential market opportunity.")
        logger.debug("Identified low density market opportunity")
    elif density_score > 0.7:
        insights.append("High restaurant density - saturated market with strong competition.")
        logger.debug("Identified high density saturated market")
    else:
        insights.append("Moderate restaurant density - balanced market conditions.")
        logger.debug("Identified moderate density balanced market")
    
    if len(restaurants) == 0:
        insights.append("No restaurants found in the area.")
        logger.warning("No restaurants found in search area")
    elif len(restaurants) < 5:
        insights.append("Limited dining options available.")
        logger.debug("Limited dining options detected")
    elif len(restaurants) > 20:
        insights.append("Diverse dining scene with many options.")
        logger.debug("Diverse dining scene detected")
    
    logger.debug(f"Generated {len(insights)} insights")
    return insights

@router.post("/market-gap-analysis")
def analyze_market_gaps(request: LocationRequest, cuisine_type: str = Query(...)):
    """
    Analyze market gaps for a specific cuisine type in a given area.
    """
    try:
        logger.info(f"Starting market gap analysis for {cuisine_type} at lat={request.lat}, lng={request.lng}")
        
        # Get all restaurants in the area
        restaurants = places_service.get_restaurants(request.lat, request.lng, request.radius)
        logger.debug(f"Retrieved {len(restaurants)} total restaurants")
        
        # Filter by cuisine type (basic implementation)
        cuisine_restaurants = [r for r in restaurants if cuisine_type.lower() in r.get('types', [])]
        logger.debug(f"Found {len(cuisine_restaurants)} {cuisine_type} restaurants")
        
        # Basic gap analysis
        total_restaurants = len(restaurants)
        cuisine_count = len(cuisine_restaurants)
        market_share = cuisine_count / total_restaurants if total_restaurants > 0 else 0
        opportunity_score = 1 - market_share
        
        logger.info(f"Market gap analysis complete - {cuisine_type}: {cuisine_count}/{total_restaurants} restaurants ({market_share:.2%} market share)")
        
        return {
            "cuisine_type": cuisine_type,
            "total_restaurants": total_restaurants,
            "cuisine_restaurants": cuisine_count,
            "market_share": market_share,
            "opportunity_score": opportunity_score
        }
        
    except Exception as e:
        logger.error(f"Error in market gap analysis for {cuisine_type}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))




































# from fastapi import APIRouter, HTTPException, Query
# from typing import List
# from models.schemas import LocationRequest, DensityResponse
# from services.google_place import GooglePlacesService
# from services.density_calc import calculate_restaurant_density

# router = APIRouter()
# places_service = GooglePlacesService()

# @router.post("/density-analysis", response_model=DensityResponse)
# def analyze_restaurant_density(request: LocationRequest) -> DensityResponse:
#     """
#     Analyze restaurant density in a given area.
#     """
#     try:        
#         # Get restaurant data
#         restaurants = places_service.get_restaurants(request.lat, request.lng, request.radius)
        
#         # Calculate density
#         density_score = calculate_restaurant_density(restaurants, request.radius)
        
#         # Generate insights
#         insights = generate_restaurant_insights(restaurants, density_score)
        
#         return DensityResponse(
#             density_score=density_score,
#             business_count=len(restaurants),
#             businesses=restaurants,
#             insights=insights
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# def generate_restaurant_insights(restaurants, density_score):
#     """Generate insights based on restaurant data and density score."""
#     insights = []
    
#     if density_score < 0.3:
#         insights.append("Low restaurant density detected - potential market opportunity.")
#     elif density_score > 0.7:
#         insights.append("High restaurant density - saturated market with strong competition.")
#     else:
#         insights.append("Moderate restaurant density - balanced market conditions.")
    
#     if len(restaurants) == 0:
#         insights.append("No restaurants found in the area.")
#     elif len(restaurants) < 5:
#         insights.append("Limited dining options available.")
#     elif len(restaurants) > 20:
#         insights.append("Diverse dining scene with many options.")
    
#     return insights

# @router.post("/market-gap-analysis")
# def analyze_market_gaps(request: LocationRequest, cuisine_type: str = Query(...)):
#     """
#     Analyze market gaps for a specific cuisine type in a given area.
#     """
#     try:
#         # Get all restaurants in the area
#         restaurants = places_service.get_restaurants(request.lat, request.lng, request.radius)
        
#         # Filter by cuisine type (basic implementation)
#         cuisine_restaurants = [r for r in restaurants if cuisine_type.lower() in r.get('types', [])]
        
#         # Basic gap analysis
#         total_restaurants = len(restaurants)
#         cuisine_count = len(cuisine_restaurants)
#         market_share = cuisine_count / total_restaurants if total_restaurants > 0 else 0
        
#         return {
#             "cuisine_type": cuisine_type,
#             "total_restaurants": total_restaurants,
#             "cuisine_restaurants": cuisine_count,
#             "market_share": market_share,
#             "opportunity_score": 1 - market_share
#         }
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


=======
from fastapi import APIRouter
from models.schemas import Restaurants
from services import restaurants as restaurant_service

router = APIRouter()

@router.post("/restaurants")
async def add_restaurant(payload: Restaurants):
    return await restaurant_service.create_restaurant(payload)

@router.get("/restaurants")
async def list_restaurants():
    return await restaurant_service.get_all_restaurants()

@router.get("/restaurants/cluster/{cluster_id}")
async def list_restaurants_by_cluster(cluster_id: int):
    return await restaurant_service.get_restaurants_by_cluster(cluster_id)
>>>>>>> clean-branch
