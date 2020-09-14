import requests
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.db.models import Count
from .models import Backups, BackupItems, CardsSerializer
from datetime import datetime
from django.conf import settings

class BackUpView(viewsets.ViewSet):

    # @action(detail=False, methods=["GET"])
    # def count(self,request,pk=None):
    #     return Response(status=HTTP_200_OK, data={"count": Backups.objects.annotate(Count("id"))})

    def list(self, request):

        query = request.query_params
        name = query['name']
        hit_point = query['hitPoint']
        rarity = query['rarity']
        response = Response()
        if not name and not hit_point and not rarity:
            response.status_code = HTTP_400_BAD_REQUEST
            response.data = {"error":"Select at-least one filter to proceed searching!"}
            return response
        
        backup = None

        try:
            backup = Backups.objects.latest('backup_on')
        except:
            pass

        if not backup:
            response.status_code = HTTP_200_OK
            response.data = {"error":"No backup exists to search!"}
            return response

        q = BackupItems.objects.filter(backup = backup)
        if name:
            q = q.filter(name=name)
        if hit_point:
            q = q.filter(hp=hit_point)
        if rarity:
            q = q.filter(rarity=rarity)

        response.status_code = HTTP_200_OK
        response.data = {'cards': CardsSerializer(list(q),many=True).data}
        return response

    def create(self, request):
        try:
            res = None
            res = requests.get(settings.POKEMON_API_URL)
        except:
            pass
        response = Response()
        if not res:
            response.status_code = HTTP_200_OK
            response.data = {"error": "Backup not successfull, Please try again later!"}
            return response

        cards = res.json()

        backup = Backups()
        backup.name = "Pokemon_Backup_{}".format(datetime.timestamp(datetime.now()))
        backup.save()

        for card in cards['cards']:
            item = BackupItems()
            item.card_id = self._get_value(card,'id')
            item.backup = backup
            item.name = self._get_value(card,'name')
            item.image_url = self._get_value(card, 'imageUrl')
            item.image_url_hi_res = self._get_value(card,'imageUrlHiRes')
            item.subtype = self._get_value(card,'subtype')
            item.supertype = self._get_value(card,'supertype')
            item.ability = self._get_value(card,'ability')
            item.hp = self._get_value(card,'hp')
            item.number = self._get_value(card,'number')
            item.artist = self._get_value(card,'artist')
            item.rarity = self._get_value(card,'rarity')
            item.series = self._get_value(card,'series')
            item.set = self._get_value(card,'set')
            item.set_code = self._get_value(card,'setCode')
            item.retreat_cost = self._get_value(card,'retreatCost')
            item.converted_retreat_cost = self._get_value(card,'convertedRetreatCost')
            item.text = self._get_value(card,'text')
            item.types = self._get_value(card,'types')
            item.attacks = self._get_value(card,'attacks')
            item.weaknesses = self._get_value(card,'weaknesses')
            item.resistances = self._get_value(card,'resistances')
            item.evolves_from = self._get_value(card,'evolvesFrom')
            item.save()

        response.status_code = HTTP_200_OK
        response.data = {"success":"Backup created successfully!"}
        return response

    def _get_value(self, card, key):

        if key in card:
            return card[key]
        
        return None

    def delete(self,request):
        backup = None
        response = Response()

        try:
            backup = Backups.objects.latest('backup_on')
            backup.delete()
        except:
            pass
        if not backup:
            response.status_code = HTTP_200_OK
            response.data = {"error":"No backup exists to purge!"}
            return response
        
        response.status_code = HTTP_200_OK
        response.data = {"success":"Latest backup deleted successfully!"}
        return response
