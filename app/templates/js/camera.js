function setControl(dest, plugin, id, group, value)
{
          $.get('localhost:8080/?action=command&dest='+dest+'&plugin='+plugin+'&id='+id+'&group='+group+'&value='+value);
}
