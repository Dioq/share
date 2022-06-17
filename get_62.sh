
ifuse /mnt/app

ifuse --container com.hanlee.top -o nonempty /mnt/app

cp /mnt/app/Library/WechatPrivate/wx.dat ./

umount /mnt/app
umount /mnt/app
