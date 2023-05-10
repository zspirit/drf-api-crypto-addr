from django.shortcuts import render
from django.http import JsonResponse
from .models import Cryptoaddress
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CryptoaddressSerializers
from bitcoinaddress import Wallet
from eth_account import Account
import secrets
# Create your views here.


def getBitcoinAdress():
    wallet = Wallet(testnet=True)
    return wallet.address.testnet.pubaddr1, wallet.key.testnet.wif

def getEthereumAdress():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return acct.address, private_key


@api_view(['GET'])
def list(request):
    address = Cryptoaddress.objects.all()
    serializer = CryptoaddressSerializers(address, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    address = Cryptoaddress.objects.get(id=pk)
    serializer = CryptoaddressSerializers(address, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    crypto = request.data.get('crypto')
    match crypto.upper():
        case 'BTC':
            address, pkey = getBitcoinAdress()
        case 'ETH':
            address, pkey = getEthereumAdress()
        case default:
            address = "Unsupported cryoto"
    request.data['address'] = address
    request.data['private_key'] = pkey
    request.data['crypto'] = crypto
    serializer = CryptoaddressSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)