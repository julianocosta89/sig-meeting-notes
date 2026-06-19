SIG: System Sem Conv Stability WG
Date: 2026-06-18
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:24 When I was…
**Roger Coll** 01:25 Hey, voila, bubble.
Natal.
**Pablo Baeyens** 01:30 Yep.
**Roger Coll** 01:34 semanitas.
Este develop. Ahora que ahi hace frio, cos vuelgo un poco al calor.
mucho calora ahora, no, oviendo.
**Pablo Baeyens** 01:50 Si, por, te finale 3 o'clock, a que esi.
**Roger Coll** 01:57 Bua, lo normal para usotro.
**Pablo Baeyens** 02:00 See, CCN.
Yeah, I see a little bit out. I would have my own… momento, pero. Si. No, yeah.
**Roger Coll** 02:11 Phenomenal.
**Pablo Baeyens** 02:12 Correct.
**Roger Coll** 02:13 Acaba de empezar,
**Pablo Baeyens** 02:18 era, y su frieble mi…
**Roger Coll** 02:25 Sir?
**Pablo Baeyens** 02:26 Naraba. No sir.
**Roger Coll** 02:27 Blah, no.
**Pablo Baeyens** 02:28 Was it?
What's up?
**Roger Coll** 02:33 No, bueno, aqui cerca de Barcelona.
Hase calor, pero no 3 a ver cuando estamos.
31, se el maximo son 3aidos, que nos.
Se estavia en su bongo.
Comparado, 20, 30 o cuarenta.
**Pablo Baeyens** 02:58 Sweet, how about… Hey!
**Kamehameha (ca-wat-brt3)** 03:01 Hello.
**Roger Coll** 03:02 Hey.
**Pablo Baeyens** 03:03 That's… That's incredible.
**Kamehameha (ca-wat-brt3)** 03:05 figure out a little…
**Pablo Baeyens** 03:07 Meeting room names.
**Kamehameha (ca-wat-brt3)** 03:09 Yeah, I couldn't find it.
**Roger Coll** 03:10 Yeah.
**Kamehameha (ca-wat-brt3)** 03:10 I couldn't find it, and now I can't figure out how to lower the desk, so I think I'm taking this meeting standing up.
**Roger Coll** 03:17 I thought it was a bot name at the beginning.
**Kamehameha (ca-wat-brt3)** 03:21 Yeah.
**Roger Coll** 03:21 Doesn't mean… Comment, comment, crap.
**Kamehameha (ca-wat-brt3)** 03:26 It's a reference to Dragon Ball…
**Pablo Baeyens** 03:30 Yeah, or two.
Wasn't that, like, a Hawaiian king? Yeah.
**Roger Coll** 03:34 Yeah, yeah, yeah, yeah, Hawaiian cake.
**Kamehameha (ca-wat-brt3)** 03:36 movies.
**Pablo Baeyens** 03:38 Yeah, I think the Dragon Ball thing maybe was inspired on the Hawaiian King.
**Roger Coll** 03:42 Probably.
**Pablo Baeyens** 03:45 I always find that funny, because I know about the Dragon Ball thing first.
**Kamehameha (ca-wat-brt3)** 03:51 We also need the Dragon Ball thing first.
**Pablo Baeyens** 03:56 you know, I don't know. Hawaiian is an interesting… Ledwich with… Although… They have very few consonant sounds, so it's very…
**Roger Coll** 04:07 Hmm, it's in there.
**Kamehameha (ca-wat-brt3)** 04:09 Flowy. Very flowy.
**Pablo Baeyens** 04:10 Yeah, I don't know how to describe it, but yeah, it's like… You don't see two continents together, for example.
**Roger Coll** 04:19 So this is pronounced Kamekameca, like, okay, Dragon Ball, now I get it.
**Pablo Baeyens** 04:30 Wow.
**Roger Coll** 04:32 That's something to leave.
**Pablo Baeyens** 04:48 Island.
occupied 15 villains.
I want to talk about, like.
Stabilizing the system namespace? Like, what?
What do we need to do, and whether we could start with Some part of it, and then the waters.
bike.
stabilizing Subset of attributes, or metrics, or something.
or… Going all the way in, because that seems… That's a learning for me from the processed thing, like… splitting things.
Seems to make sense, and we'll probably find some… Blockers, like these three attributes along the way.
**Kamehameha (ca-wat-brt3)** 06:22 Something that would probably… help, and it's kind of gonna have to come from me, is I had a PR open… like, our System SemConv docs, that was, like, explaining our idea of, like, sub-areas, where we have, like.
System, and then a sub-area system memory, and… When you put something in system.memory, we're saying, this is… Memory statistics, but they're nominally reported against a host.
So, like, when a host is tracking its own memory statistics, or, like, system paging is about the system doing paging, and then there's… like, that's sort of, sort of trying to un… detangle this idea of, like, there's a CPU namespace and a system.cpu namespace, why do they both exist?
I have that PR open. It was opened a long time ago, I think even before KubeCon, and it had, like, 10 comments from Thompson Tomo, and I couldn't bring myself to look at them, so the PR died.
**Pablo Baeyens** 07:23 Yeah, I guess that would help, yeah.
**Kamehameha (ca-wat-brt3)** 07:32 But if I could… if I could go back and… and try and, like, appease the… the overlords to get that… that PR merge, that would probably help guide us, because then we could start to tackle it In, like, a subsystem way, where, like, We could say.
Let's look at all the memory and system.memory, and try and… Try and stabilize everything related to memory, but in both the memory namespace and the system memory namespace.
**Pablo Baeyens** 08:03 Yup.
**Kamehameha (ca-wat-brt3)** 08:08 And it might, it might be that… The system namespace still has stuff that kind of goes counter to the way we want to do it now, because, like, it started out as the system namespace was just… I was just, like, where we put system stuff, because, like, that's what our group was called. We just kind of threw some.
**Pablo Baeyens** 08:24 Nothing.
**Kamehameha (ca-wat-brt3)** 08:25 And now we're actually trying to say, this has a meaning. This means it's something reported against a host OS. Like, a host… like, stuff related to how the host OS is… what's the whole, like, what's the host system's CPU time? That's why there's a system.cpu time, because the… a CPU itself does not have a CPU time, but a system is tracking the amount of time it spends on a CPU in different states, so it doesn't make sense for… there to be CPU time, because in the CPU namespace, it's about stuff that's about, like, a literal CPU unit versus about a system that interacts with it. That's… I think I just need to, like.
finish codifying that sort of idea to alleviate confusion. It would have… it would have helped to be able to point to it when it came to this whole system paging debate that happened.
That is… like…
**Pablo Baeyens** 09:19 Yo.
**Kamehameha (ca-wat-brt3)** 09:21 It really could go either way on it, but realistically.
The word paging, it already implies memory.
And… It is not… physical memory that does paging. It is… host operating system loading pages into memory, and the system is what manages pages. So it's called… it should be called system.paging, realistically, I think.
So I think probably it's kind of on me to just, like, finish Writing down that philosophy, and then we can apply that to everything from there.
**Pablo Baeyens** 09:56 Okay, are there any dependencies between the namespaces? I mean, like, is there… The system don't… File system depend on… so on us.
**Roger Coll** 10:11 the CPU, we have the CPU mode, right? It's not…
**Pablo Baeyens** 10:16 So we have the system CPU, depends on CPU, okay, but is there any other… I guess…
**Roger Coll** 10:24 Huh.
**Kamehameha (ca-wat-brt3)** 10:24 Actually, yeah, file system depends on disk, I think.
**Pablo Baeyens** 10:28 Let me check.
**Kamehameha (ca-wat-brt3)** 10:29 I can't remember. I haven't looked at those leases in a long time.
**Pablo Baeyens** 10:33 So… let me…
**Roger Coll** 10:36 That's this…
**Pablo Baeyens** 10:36 I don't know.
**Roger Coll** 10:37 I.O. direction…
**Pablo Baeyens** 10:39 Simple U.
**Kamehameha (ca-wat-brt3)** 10:41 Is there a disk IO direction file system? Like, for, like, bytes written to files, to, and read from a file system? I don't actually remember if that's tracked.
**Roger Coll** 10:49 Me neither. Let's check.
**Pablo Baeyens** 10:51 Yeah, so system disk I.O. depends on disk I.O. direction… okay, let me…
**Kamehameha (ca-wat-brt3)** 10:56 And that… that part still sort of aligns with what we're… trying to say for our philosophy, because, like, a disk I.O. direction is, like.
That's a… that's the property of a… of a disk, I guess. I don't know, it's kind of nebulous, but, like, the attributes being in just the disk, rather than being in system.disk.
You could start to really woodshed it deeply and say, like, should a disk device name… be under system or under disk.
Because… the disk itself, As a name only because the system assigned it one.
**Pablo Baeyens** 11:36 Yeah.
**Kamehameha (ca-wat-brt3)** 11:37 That starts to get a little hairy. I don't actually know the right call. My instinct still wants the attributes to just live in disk, but… I need to.
**Pablo Baeyens** 11:46 I mean, right now we have system.device, so…
**Kamehameha (ca-wat-brt3)** 11:50 Oh, I forgot, we just have one device identifier, yeah, like, one device attribute?
Is that gonna.
**Pablo Baeyens** 11:55 Oh yeah, it's system.device, which is the device identifier, is the description.
**Kamehameha (ca-wat-brt3)** 12:01 because I guess… In Linux, at least, all device identifiers are kind of… kind of the same thing, but, like, I think we use system.device in, like.
For, like, network interface metrics, for disk metrics?
Maybe it's fine.
**Roger Coll** 12:21 Hmm… For the network, we use network interface name.
**Kamehameha (ca-wat-brt3)** 12:29 Oh, we don't use device for the network.
**Roger Coll** 12:32 No, at least for the packet.
**Kamehameha (ca-wat-brt3)** 12:35 Okay.
**Roger Coll** 12:36 Yeah, nor the… nor the network errors.
Yes, all the system, let's say, network metrics seem to have network attributes.
So… But it… I guess it makes sense, right? For the process, it seems that we do the same, so the metric starts with system, but then The attributes, it's just on the process.
Name a space.
**Kamehameha (ca-wat-brt3)** 13:02 Yeah.
like, the… I remember we moved… System.process.state into just being the same attribute as process.state, because… Like, the process is the one that has the state.
**Pablo Baeyens** 13:20 And, So I think all of the dependencies from something that is in the system namespace to something that is not would be system CPU depends on CPU, system disk on disk, system network on network, and system file system depends on file.
I just wanted to do that so that we now know… Is there another… area of semantic conventions that is also using the disk thing, and that we need to get the approval from, because I think that's something that us.
**Kamehameha (ca-wat-brt3)** 13:53 Right.
**Pablo Baeyens** 13:54 It's an us now with the process thing, so probably better to…
**Kamehameha (ca-wat-brt3)** 13:58 A common one is container. I think we share a lot of this stuff with the container namespace, which… is not… not that weird, because I think a lot of the container metrics are designed to be largely the same thing as…
**Pablo Baeyens** 14:14 Huh.
**Kamehameha (ca-wat-brt3)** 14:14 A lot of the process metrics and system metrics, but…
**Pablo Baeyens** 14:19 Yeah, yeah, so this guy, your direction, for example, yeah, it's container metrics as well.
Okay, so, container…
**Christos Markou** 14:40 Those should be easy, though, even if we have, like, the benches or conflicts.
Yeah, I think we have the Cates SIG as well, that I also participate, so it should be fairly easy to move faster if we need anything.
**Pablo Baeyens** 14:58 Okay.
**Kamehameha (ca-wat-brt3)** 14:59 No, I'm… the network… the network group now has a say for anything network-related, but I've been working with them on getting the network I.O. direction.
Dot, Finalized and stuff, too.
So hopefully we are remaining involved in all the spots where we might share dependencies along the way. Profiling is probably the only one Where we have to… like, put them in if we do anything in, like, the file namespace. I know they use some metrics in, like, process and some metrics in… in file, sort of, like, for identifying files on profiles.
So we'll have to keep them looped in, but I think… I think they kind of… We're aware that we're trying to stabilize this stuff, and so they should be responsive.
**Pablo Baeyens** 15:51 Yep.
Okay, then in terms of entity… Entity Associations.
Oh.
**Kamehameha (ca-wat-brt3)** 16:02 I'll hook that.
**Pablo Baeyens** 16:04 Yes.
host, right? It's just… There's nothing else.
**Roger Coll** 16:17 post.
**Pablo Baeyens** 16:17 But…
**Roger Coll** 16:18 process.
**Kamehameha (ca-wat-brt3)** 16:20 Another one is hardware.
**Pablo Baeyens** 16:21 Oh, Yeah, I'm looking at the system metrics right now, and I don't see any… any other entity that we have defined so far that's not host. The process metrics we have the…
**Kamehameha (ca-wat-brt3)** 16:36 Yeah, I don't think so.
I'm not…
**Pablo Baeyens** 16:38 Nope.
I don't know if we know.
**Kamehameha (ca-wat-brt3)** 16:42 need of you right now.
Although we… we could probably do with some fix-ups on… on host, maybe, but…
**Pablo Baeyens** 16:53 Okay, and… Sorry, I forget. Do we need to mark the entity as stable before we can mark the… Metrics are stable.
**Kamehameha (ca-wat-brt3)** 17:08 Or we can mark the metrics as stable, we do need to mark the entity as stable, yeah.
**Pablo Baeyens** 17:12 Okay.
**Kamehameha (ca-wat-brt3)** 17:13 You can stabilize It's not… my understanding.
**Pablo Baeyens** 17:16 We can save lives.
**Kamehameha (ca-wat-brt3)** 17:16 is attributes, entities, metrics.
**Pablo Baeyens** 17:20 Okay.
Okay. That is a bummer.
**Kamehameha (ca-wat-brt3)** 17:30 Is it… is it finally time for us to run headfirst into the host.id debate and, like, finally… Finally solved this.
It's still… it still… it still bugs me, but everybody uses it.
**Pablo Baeyens** 17:47 Yeah, I think… I think that's the best thing we can do right now, because we… at least I would propose, like, we have this VR for stabilizing the attributes that we need to stabilize the process stuff.
Probably… Waiting and seeing how that develops is the best we can do there, and once we have that, we can think about Do we move forward with other attributes? And in parallel, we can talk about the host.
Yeah, I think… Okay. Yeah.
**Kamehameha (ca-wat-brt3)** 18:30 From the network group side, I think that we're almost… we're almost finished.
Some of the people who are offering to lead the network group right now, I think they actually don't really… fully understand the OTEL data model.
They were very concerned about the attribute when they first looked at it, but it was because… They thought it meant that we would maybe report a metric where we're only reporting read and not write.
for, like, a network… for, like, an I.O. direction thing, I don't know, I kind of had to, like.
Explain to them how the… how the data model works, but I think they're okay with it now that I've explained it.
**Pablo Baeyens** 19:09 Okay, so, yeah, then I guess we should talk about host ID, because… To stabilize an entity.
Who would basically need to define the identifying attributes on… dots… Sweet, yeah.
**Kamehameha (ca-wat-brt3)** 19:32 the identifying attributes have to be stable. I think that's the guaranteed thing. I don't think every opt-in attribute has to be stable.
I don't think. If that… if that's… not the case. I think we should raise an issue. I think the important thing is that the… the, Though… Required identifying attributes have to be stable.
**Pablo Baeyens** 19:56 Yup.
**Kamehameha (ca-wat-brt3)** 19:56 But host ID is one of them.
**Pablo Baeyens** 20:01 Is social identity the only one of them?
I guess so.
That's fine.
**Kamehameha (ca-wat-brt3)** 20:07 Probably. Post ID is a weird one. Okay, I… my… I've never known where I land on this, but… like, we… what we tend to say is that host.id should be like, Etsy machine ID?
For, at least for a Linux host.
What people are doing right now is they're taking like, whatever, like, VM provider they're using, and, like, whatever the global identifier is for that provider, putting it in host ID.
**Pablo Baeyens** 20:39 Yeah, I mean, that's actually the way it is defined right now. It's like, if you're on a cloud provider, you must use the instance.
**Kamehameha (ca-wat-brt3)** 20:45 Oh, okay.
**Pablo Baeyens** 20:46 Bye-bye.
**Kamehameha (ca-wat-brt3)** 20:47 So that's the… that's the…
**Pablo Baeyens** 20:51 And if you're not, then you should use the…
**Kamehameha (ca-wat-brt3)** 20:55 And fallback.
**Pablo Baeyens** 20:55 the machine ID, you know.
**Kamehameha (ca-wat-brt3)** 20:58 that just feels… it feels off to me, like, the fact that host ID… could have an ARN, or could have a, like, a… GCE instance ID, or, like, could have anything.
but…
**Roger Coll** 21:14 Yeah…
**Kamehameha (ca-wat-brt3)** 21:15 But is machine ID useful, though? Like, seeing a machine ID in your metrics backend?
Is that actually useful? Because if I looked at a machine ID without other information, I wouldn't know what machine I'm looking at.
**Pablo Baeyens** 21:32 I… I'd be interested on the Elastic people's day, because I believe you do use Machine ID to some extent.
**Roger Coll** 21:44 No, I think we rely a lot on the host.name.
And we use that for mostly everything, but there's… two kind of host names, if I remember correctly.
**Christos Markou** 21:57 He's…
**Roger Coll** 21:59 Let me check, I think I opened an issue a while ago explaining all of that.
No, because the machine ID, if you are not on cloud, or you are not using some, specific distributions, at least for Linux.
you might not have it. It's not… part of the Linux kernel, this value, just, something that the distributions came.
But… Yeah, I'm gonna share the issue, but I don't know if it's very, very related with the… Here's the host ID discussion? It's more on the host… host.name.
**Pablo Baeyens** 22:57 I have my own issue that I filed a couple of years ago.
Yeah, so, I guess, some context, dates are the… Build some of the products using The number of hosts, it builds you by the number of hosts, so it's rather important for us to The names of the things that we're billing you for.
The… so I've spent some time looking into what we use, and I feel like That's probably representative of what people would want to use. There's… So… On EC2, for example, I think there's 3 things you would have, which are the instance ID, the operating system host name, and the machine ID, and One problem that we face… And I guess it's… not specific to Datadog is that, the friend… approaches, do not have access to all of those host names. So, for example, if you're using the AWS APIs to fetch information about EC2 machines. You do not have access to run arbitrary commands on them, so basically you have the instance ID, and that's it. And if you're running on it, then you may be able to access the other ones.
Although, you may not be able, if it's, like, containerized or something, you may not be able to get the operating system hosting.
And… I tend to become a bit of a… nihilist about this, like, I don't think there is such a thing as a host ID that can be defined in a reliable way.
**Kamehameha (ca-wat-brt3)** 25:05 It's, it's cause, like, nominally.
identifying a host depends on what scope you're trying to identify it within. Like, if you have your own, like, Proxmox rack, you know, you have your own ID, within that, and then if you're in AWS, within your project, you have IDs, within… like, whatever VM provider, so, like, identifying a host does depend entirely on what context you're trying to identify it within.
So it's kind of hard to just say… this is exactly what host ID should be, so it… It might be that my concern is unfounded, and we should just stick with Was what we've been doing, basically say, like.
for host ID, it just has to be, like, identifying within whatever context you're trying to identify the machine, and that's kind of up to you. We can't decide.
generically, in SEMConv, at all times, what what host ID should exactly look like, just what it should principally be.
**Pablo Baeyens** 26:10 Yeah, I think, to me, the… two alternatives that I see reasonable are either we keep things as they are, or we add cloud provider-specific attributes for the… different ways of naming machines on each cloud provider, and we keep host ID for something like machine ID.
That would be the other option.
**Kamehameha (ca-wat-brt3)** 26:43 So… One thing… so, like, the last time we talked about this was before this idea of, like.
Joining entities was a thing, where you, like, report multiple entities on your signal, and they're kind of joined on some… on some field.
I kind of like the idea of, like, we have our host entity, and host ID could have, like, an AWS instance ID, or a GCE, or Proxmox, or, like, whatever On text you're in.
And then Alongside it, you could also report like… an EC2 instance… entity.
that would have a cloud instance ID, That is, like, the AWS one, and it would join on host ID.
That makes me feel a bit more… okay with host ID being, like, any old type of identifier, like, we don't know what it's gonna be, because… You can report more details in entities that are reported alongside the host.
The normal host one.
**Pablo Baeyens** 27:50 Sorry, I'm not sure I got it. So this is the telescoping identity thing? Or…
**Kamehameha (ca-wat-brt3)** 27:56 Yeah, that's what it's called. I don't understand why the word telescoping is used, because I might not even be fully understanding the proposal properly, but what I'm thinking of is… Basically, you don't need… You can drill down into more details, not by just overloading one entity with a bunch of attributes. Instead, you say.
there's another entity that's gonna be reported in, like, the array of entities on the OTLP.
And there's some field that joins the two.
like, with process, this is kind of what we're doing with process executable. There's all these process executable attributes on process, and to avoid, like, clashes with how you identify it, we take the process executable stuff into a process executable entity that joins on Some field, or, like, it's reported alongside so that you know that this process Also has this executable, like, it's related to.
**Pablo Baeyens** 28:55 Bad.
**Kamehameha (ca-wat-brt3)** 28:56 M.
And we could kind of do the same thing with host, where you have the general host entity that looks the same no matter what provider or VM context you're working on.
And then alongside it, could be… an entity that's designed for that provider. So, like, there could be an EC2 entity.
There could be a VMware entity, there could be a GCE one, you know, whatever we're deciding to do.
**Pablo Baeyens** 29:20 It would be.
**Kamehameha (ca-wat-brt3)** 29:21 We… the idea would be to report it a… like, if you have all your system metrics in a payload, your entities would have two entities. One would be a generic host one, and one would be… more details specific to, like, I'm an EC2 instance, and they would both be there on the signal, but in separate entities.
backend could then figure that out via matching host ID to, like, cloud.instanceID or something, or some field.
the exact way you define those relationships isn't really figured out yet. I… I don't even… I don't think Weaver supports it or anything, but my thought was that you would… you would define like, a relationship for, like, within Host.
There would be a bunch of different relationships, like, is, And that relationship could be, like, is a EC2 instance is an option, or is a VMware instance is an option, or is a… Something or other.
**Pablo Baeyens** 30:18 Okay, and for host ID, then, we would keep… Things as they are right now.
Basically.
**Kamehameha (ca-wat-brt3)** 30:25 So, yeah. So, with the ISR relationship, presumably there would be some field that you'd join on.
And we would say that field would be host.id, And so, host.id would be… Same as the EC2 instance ID, And then the EC2 instance entity also has that same ID in, like, a cloud.instance.id attribute or something, and they…
**Pablo Baeyens** 30:48 Huh.
**Kamehameha (ca-wat-brt3)** 30:48 Going together on those values being the same.
**Pablo Baeyens** 30:53 Okay, yeah.
**Roger Coll** 30:57 So, we would remove the cloud definition from the host ID, or…
**Kamehameha (ca-wat-brt3)** 31:04 I think we would keep it. So, that… the ambiguity that I always had a problem with, of, like.
host.id is one attribute that could have, like, 10 different ID formats, and we don't know what it is.
like, just by looking at a host entity, we don't know, like, is this an EC2 instance ID? Like, we only know by virtue of, like, we instrumented our environment, so we know it is, but, like, what if you're in a multi-cloud setting, you have a bunch of host entities with a bunch of, like, random-ass host IDs, how do you figure out what's what?
But with… if you can have a related entity, And you say.
the host ID that I reported here joins on the cloud instance ID of this other entity of, like, this is a GCE instance, and then this is an EC2 instance.
then the backend… the host ID would be the same.
as the instance ID on each of these, like, other entities that it could also be.
And could… and the backend could know how to join those. And so… I am sort of, like, inventing what a backend is gonna do with entities right now, because none of… this is all very nascent.
But… My thought was that a bunch of… The backend would be receiving and recognizing a bunch of different entities by their identifying attributes.
then have knowledge of the sorts of things that it could join on, so if you look at a particular host in a backend.
and it happens to join with some GCE instance entity as well, then it would figure itself out, and be like, okay, this host entity is actually a GCE instance, and here's all the information joined together.
**Christos Markou** 32:43 My main issue all the times, when we come to this discussion is what happens when you have nested, kind of… virtualization or provisioning, for example, you can have a GCE machine, and then inside there, you can have, let's say, a VM, and then inside the VM, you have something else. So, should… all the host… so, if you run the collector inside the very internal, host thing, should not come with the ID of the very external, cloud instance, for example. So, this… for me, I tend to believe that we need an extra thing, like cloud instance entity, or something like that. It could be per provider or generic, but host itself is what we see as a host. So, if I run the collector, for example, inside the host, inside this machine, what I will observe.
I know we have this component, the research detection processor, that can detect if it runs as a cloud instance or something like that, and add additional things.
But if we keep this out, maybe we need to, like, discuss this from the perspective of entities and specification itself, rather than what implementations right now do, because maybe the implementations are wrong, and they will change based on entities' outcomes.
Yeah, true.
Yeah, still… I'm still struggling to put this together in my head, but I think it's confusing what we have now.
I agree.
**Kamehameha (ca-wat-brt3)** 34:18 Yeah, the… the layering problem that you mentioned is a big reason that I actually have never really liked the word host for this.
Because host is a nice word when you're talking in a virtualization sense. It's like, you have the host, and you have the things it's hosting.
like, the containers. So that's nice when you're thinking of Kubernetes, and it's like, you have the host, then you have all the different containers that are being orchestrated under that host, but when it comes to, like.
**Christos Markou** 34:44 That is the node, though, it's not a host.
**Kamehameha (ca-wat-brt3)** 34:48 Well… Right, there could be multiple nodes on a host, I guess. I don't… I don't… I don't… I don't really know… Kubernetes all that well, but…
**Christos Markou** 34:57 I mean, the terminology that you should use in that case is the node, so relationship is node to… node to pods, for example. Right. Something like that.
**Kamehameha (ca-wat-brt3)** 35:10 the word… The word host always… always is… because, like, you could… the scenario you mentioned is entirely possible, like, you could take a GCE VM, which is already… like, even a VM provided by a provider, like, it itself is not the host either. Some rack machine in a data center is the host.
And then that VM… but then that VM could have its own… its own VM provision, and you actually could just kind of… continue to nest that. And so, in that case, what is the host? Like, where… where do we draw the boundary? And the… the way I try to think of it is, like.
Wherever you're instrumenting, knows its own context. So, like, if you instrument like, an EC2 instance or something.
It knows that it is a… System, like, it has… access to syscalls somehow, like, maybe it's behind a hypervisor or something, but, like, it has access to some kind of syscalls to get information about itself. It can't figure out That it is not… true… the one true host, where the one true host is, like, some bare metal rack in a data center somewhere, but it can know itself.
And that would then be true for, like, the next layer. Like, if you've instrumented within a VM in the next layer.
Can't figure out things about… like, unless a virtualization runtime allows it to, it can't figure out much about what's outside of it, but itself, it knows that it is able to collect information for, like, here's my… these are my disk stats, these are the processes running within me, these are my process stats.
and the… Bit.
So, the thing that I talked about with, like.
we would have, like, a cloud instance entity or something. The is-a relationship would sort of facilitate for, like, figuring out at what level we're talking about, because if we're talking about an EC2 instance, and then, like, maybe that EC2 instance is also Proxmoxing, like, 5 other VMs or something.
Like, that… we might have an… if someone decided to come up with semantic conventions for them, like, I am a virtual machine in this type of virtualization layer, and that would have its own is-a relationship, so we wouldn't call that host entity, which would be able to fetch all the other instrumentation information about itself.
We wouldn't call that a GCE instance, though, because it's not. It is a Proxmox instance within something else, but it can at least figure that out and report, like, that it is a Proxmox that it is reporting from itself.
That's… this is why I hate the word host, though. Host is… is a… is… Not a great name when we're… When we're just talking about, like, a normal machine.
**Christos Markou** 37:58 shouldn't entities, have an answer on this? Because I remember they had this notion of.
observer or observation point, some, I don't remember exactly the terminology, and… I'm pretty sure that they had very similar examples there, so… I'm not sure if they can cover exactly what we're discussing here, but to me, it looks like an entity's problem. Yeah.
Push to meet you.
**Kamehameha (ca-wat-brt3)** 38:26 This would have been a good one for him to be here for.
**Pablo Baeyens** 38:30 Yeah, I mean, the issue I opened, I… tried to push for the entities group to discuss, but they didn't really do it.
**Kamehameha (ca-wat-brt3)** 38:43 The entities call is happening right now, we could always go crash it and say, hey, we talked about entities for, like, a million years, wanna… Talk about one.
**Pablo Baeyens** 38:52 I'm free!
Right now, I'm in…
**Kamehameha (ca-wat-brt3)** 38:56 Let me look at their agenda. If their agenda is packed, we can… we can… Do it later, but… No, come in.
**Pablo Baeyens** 39:05 No, it doesn't seem like it's happening right now.
**Kamehameha (ca-wat-brt3)** 39:09 Is it not? Maybe they moved it. I always thought it was right after this.
**Christos Markou** 39:13 No.
**Kamehameha (ca-wat-brt3)** 39:15 No, you're right, it's not.
**Pablo Baeyens** 39:17 It used to be, at least, right after this, yeah.
**Kamehameha (ca-wat-brt3)** 39:20 Okay, nevermind then.
Well…
**Pablo Baeyens** 39:23 It…
**Kamehameha (ca-wat-brt3)** 39:25 Josh is super stressed this week, but I might bug him about it next week.
**Pablo Baeyens** 39:29 Okay, it's happening on Mondays at 9.30am Pacific.
So…
**Kamehameha (ca-wat-brt3)** 39:37 Oh, yeah. That's a… I can… I can make that work.
**Pablo Baeyens** 39:45 I've been done.
would be really useful here, because I agree, like, this sounds like an entity.
**Kamehameha (ca-wat-brt3)** 39:55 Yeah, if I can somehow find time, I can try and, like, write up My understanding of what entities will allow us to do to enable us to actually model this.
**Pablo Baeyens** 40:07 I think the… system CPU versus CPU thing that you mentioned is more… Important right now?
**Kamehameha (ca-wat-brt3)** 40:16 Yeah, probably.
**Pablo Baeyens** 40:18 on the Yodawan.
**Kamehameha (ca-wat-brt3)** 40:19 Try and revive that PR, then.
**Pablo Baeyens** 40:22 The other one, like, depends on whatever… the entities people say, I guess.
**Kamehameha (ca-wat-brt3)** 40:30 Okay, makes sense.
**Christos Markou** 40:32 Folks, I need to jump, see you.
**Pablo Baeyens** 40:34 Yep.
See ya. Here we go.
**Kamehameha (ca-wat-brt3)** 40:37 everyone.
**Pablo Baeyens** 40:37 Successful. Right.
