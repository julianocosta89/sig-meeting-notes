SIG: eBPF instrumentation
Date: 2025-07-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Mattia Meleleo 00:00:48 Hello!
Mike Dame 00:00:50 Hey? How's it going.
Mattia Meleleo 00:00:53 All good.
MM Mario Macias 00:01:13 Hello! Everybody!
Mattia Meleleo 00:01:16 Hello!
Mike Dame 00:01:17 Okay.
Tyler Yahn 00:01:27 Blue!
How y'all doing.
MM Mario Macias 00:01:34 Hi. Emmanuel.
Tyler Yahn 00:01:36 Doing well, Nicola, how was Canada day.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:41 Yes, I'm still wearing my shirt.
It's party straight through the night. Huh!
Mike Dame 00:01:49 We don't get shirts for 4th of July.
Tyler Yahn 00:01:54 Mike, have you been to a truck? Stop before.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:57 Yeah.
Mike Dame 00:01:58 That's true, I guess. Oh, yeah, that's not 4th of July. You can get those anytime.
Tyler Yahn 00:02:01 Yeah.
Mike Dame 00:02:03 I'll need a shirt.
Tyler Yahn 00:02:06 Yeah, I gotta. I gotta get stocked up on my shirts. I gotta get a American flag one, although just just a heads up flag code specifically says you are not supposed to do that, but you know, whatever.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:19 Oh, yeah, I'm not supposed to wear my shirt here at the.
Tyler Yahn 00:02:21 No, it's a Us flag code thing like it's just, it's a it's no one actually pays attention to it. Everyone.
Kenya, yeah. Where's it as? Where's his clothing?
But yeah.
well, cool. We could probably get started here in just a second. I see there's a few items on the agenda. If you haven't yet already, go ahead and add your name to the attendees list. And yeah, we can get started here.
Awesome.
Okay, so welcome everyone, Mike. It looks like you want to start us off by talking about the probe Api and go auto usage operation steel thread.
Mike Dame 00:03:14 Yeah. So this was you know. Tyler came up with the steel thread term. I threw operation on there because I think it sounds cool, but from the Go auto sig yesterday. We've been talking a lot about the probe Api, and really trying to get some momentum and some movement behind that.
I think our original approach kind of just going from conceptual you know, design in the the Go auto project itself of trying to think of what is everything that could be supported was a little broad for us. We've tried kind of working on the you know we've made some changes to try to change that framework itself and maybe build the probe Api around that. And from discussing yesterday we thought that maybe the best approach would be to try to get a drop in probe imported, like as a proof of concept into ob a probe is the the term for the entire like representation of an instrumentation within. It's kind of an overloaded term, I know, you know, because we got you probe K probe, but capital. P. Probe is what we call these things. These definitions. So that will be we're calling it the steel thread, because it will link.
You know what the probe Api needs to be into? You know what ob expects from it?
and kind of coming off of that. There was some questions, I guess, from our side. You know me and Ron on Otigo's people trying to understand how the usage of the the Api itself, but also the go Evpf auto repo. And and that machinery was gonna be used. I yeah, I feel like I I've you know, haven't been super active in the discussion here, so I might have missed this. This is like reiterated, if you guys have discussed it before. But kind of, I guess one of the concerns that we have is making sure that the the probe Api itself and more specifically, I think the implementation in Obi isn't duplicating you know, probe management, and loading and running that is in in go auto. And if so trying to find a a consistent thread between there, because that was, you know, a a big part of the donation was making sure that we don't duplicate that that effort. And add that confusion. So I guess. Yeah, that was that was kind of the the topic, I think. Getting this poc probe put together is, I I think, our our top task here, and from that we can kind of see. How are these probes used in Obi. What functionality is needed within a probe and from there kind of suss out, okay, what should live in go auto. And what is the extra functionality built into to ob so I know ron is ron message me that he's trying to join right now, and having some issues with Zoom. But Tyler, is that, do you think kind of sums up the discussion that we had yesterday? Is there anything that you'd like to add.
Tyler Yahn 00:06:46 No, no, that was that was good. Thanks for for dropping us in. Just to be clear, I think. Someone is going to try to work. Mike. Mike was taking up the the task of trying to work on this like getting a probe in, but I'm sure we could use some help understanding like code in Obi. So just yeah, I guess maybe in the next, you know, few weeks we'll be pinging people here. I know Raphael has been working with Mike as well asynchronously for this other probe stuff. So maybe like.
And and Nicolavis, you're part of the other Sig as well, so like, I'm sure we'll have collaboration going forward. But yeah, just kind of, I think, as a high level. That's a great overview of the plan.
Mike Dame 00:07:25 Yeah. And so I'm gonna put in here. I mentioned yesterday, my, I'm gonna make an issue to kind of centralize that work around it?
and then we can collaborate through there. Asynchronously, or decide from there. But yeah, I I think, coming off of that big thing to think about, and maybe we can kind of clarify here was ob just to clarify is not going to be importing any of the like. The new instrumentation function that's in Go auto right now is that the plan.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:02 I mean, we don't.
I mean, I yeah, I don't have a concrete plan. We can do whatever we feel like we should actually do in respect of reusing the code.
So this last week and this week in Grafana we have a hackathon week. So for this hackathon week, I decided to actually try bringing a probe from. I was going to do the pedestrian way first.st It just kind of move and try to make one work. I sorry I missed a meeting yesterday. I was going to report on the things that I found were kind of challenges.
and I don't see how we can actually work to resolve them.
the one that I picked up is the one that's missing in ob right now, which is the perhaps maybe it wasn't the right choice. But either way, I picked the one that's the go SDK instrumentation to be able to use manual spans.
So that's not in Obi, I want to see what it would take to actually take the code from, or the implementation from.
go auto and make that work inside. Ob yeah, I don't know how you want to do this. I do have like a sort of a summary which is in my head right now. I haven't actually wrote. Written it down anywhere, but we can walk through that if you want now, or
Tyler Yahn 00:09:31 Yeah, I if if you.
if you were willing to to walk through that, I would be very interested in seeing that. But obviously it's putting you on the spot. So.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:41 Oh, no, absolutely. I don't mind like maybe it's still not in a sort of like a really consumable state. My thoughts are on being fully
Tyler Yahn 00:09:53 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:53 Where did I start? Okay? So I can share my screen here.
See, if you see an see anything.
Tyler Yahn 00:10:08 I don't see anything yet.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:10 I apologize if you see anything private, but you're probably not right.
Tyler Yahn 00:10:14 Yep, looks good. Yep.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:16 Okay. So this is what I set to do so it's gonna be okay. Oh, sorry. Don't do that.
That was gonna be like.
Did I stop sharing.
Mike Dame 00:10:30 And you're sharing zoom, I think.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:33 I don't know what happened. Sorry about that.
Okay.
Mike Dame 00:10:37 Yeah, we can. It looks good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:41 So what I wanted to do is essentially take this probe.
thought, your yeah, this is the one and let's see, see, how do I actually use this inside? Ob, it seems so self-contained.
And I started by saying, Okay, if I try to modify or implement what you're doing, Mike. That's gonna be hard. I was just gonna see like, what if I just took the code and moved it over? What am I gonna encounter and what are the kind of challenges that I'm gonna have to face?
Having said that, let me zoom in a bit because it's kind of like difficult to see And so there's 2 approaches. We can take. One approach would be to just vendor the source just like we're doing vendoring will be into Bela.
So pulling the source from go auto, and we just use it at a source level with meaning that within ob, we're just building to go glue around it.
And we're using the Ebpf files. So we're not actually using. That's the 1st approach we're not using the probe itself we're using just the Bpf side.
The other approach would be if we try to actually use the probes directly.
So I'm gonna walk, maybe through one example of what I had to do.
So I didn't take this code with a field tracer id, because this relies on the old maps which my latest goal version, there's a support. So it wasn't working. We need to implement the the Swiss map support.
So I kind of skimmed over that and so but let's let's see what it would take to kind of get this to work, at least that the probe initially you get everyone okay with this, where I'm going with this.
Tyler Yahn 00:12:53 Yeah, yeah.
MM Mario Macias 00:12:54 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:54 Yeah, yeah.
Okay, so the 1st thing that that is sort of different is the multi-process support which these kind of offsets don't work in ob.
because this tracer delegate position, for example, is a constant that's loaded in the probe Api for Epp. So for all go auto.
because it's 1 to one mapping of an instrumenter and a process correct. So technically, there could never be 2 offsets.
So if you look what happens in ob for the same sort of I guess this is ob yeah. Sorry. Let me see, I call the file go SDK here.
So yeah, I reuse the tracer side. But 1 1st thing that we need to do is figure out how we're going to support this. So Obi has this constitute of an offset table.
So this table is a Bpf table which gets populated instead of a constant. It gets populated for every process, and it gets updated and removed, based on processes coming and going because it can monitor multiple go process at the same time.
So offices are handled differently in our code base.
Tyler Yahn 00:14:38 Is this something? Yeah, yeah, this that makes sense. Is, is this the offset table is just like an Ebpf map.
Yeah, or is okay, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:47 Yeah. So if you look at what offices table is really is just that this go offsets map, which has an Id, and this id is a pid
Tyler Yahn 00:15:00 Oh, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:01 It's the process id for the upper bits.
and then the lower bit is the offset index in our table that we want and then, or maybe that con is wrong. Now.
Maybe that's wrong.
Tyler Yahn 00:15:20 That's fine. Yeah, I think this makes sense, though. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:23 Right, it's per pid. And it contains this, I guess we do this core read, which we find. Yes, okay, so this is wrong. Now, maybe with some early implementation, we got to fix the comment. It's going by the inode number.
right? Because the pit is kind of an overkill at the end of the day offset is tied to an executable.
So we've optimized. I think 1st implementation might have been a process id on this offset thing. But then we were like, well, why, if I have multiple executables launch from the same file like.
then it's really tied to a file.
So we read this. I know number for a given executable and then sets it up so the user space and it will be when it loads for the go tracer.
Does this.
I think, in general, this is the the sort of the main thing we gotta work around the rest.
I thought it was more or less approachable. The other thing is our use of maps?
So there's So in in go auto. In the moment the map that handles the sending of the event from Evpf to user space is a perf buffer which again is allocated once per executable and we have a shared one, obviously, because once per executable can get really it's because of the memory pressure, and and so on.
So then the question is, we would have to.
but that's an easier one to work around. And I'll explain how this works in in Ob.
and but it would take us moving some of this functionality into go auto if we agree to do so.
So if you look at the where is the ring buffer?
Here now, I'm should be in common King ring buffer.
So the important thing to note is this thing be left in internal this is a non standard way of sharing maps that is implemented here essentially.
we even in Ebpf go auto instrumentation.
Mike Dame 00:18:17 We have multiple.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:19 Programs right? And all this probes or probes may need to share maps.
So the way that's done is through typically an Ebpf through mounting a file system, the Bbpf file system.
and then allowing this map to be shared among the different probes.
So this poses. One particular challenge is that if you do that, then you need to mount this file system, and if you want to do it automatically, you need system admin permissions, and we try to avoid that as much as possible because of the security restrictions and customers won't let us do this, and so on.
So we initially were using the Bpo file system. But then we removed it. And Raphael came up with this concept essentially.
since technically they're separate probes. But they all live within the same process.
Right? All this maps.
So we have this in PIN internal, which all it really does. It lets the ob user space change the file descriptors as the Bpf programs are loaded.
So technically, as soon as the one Bpf program loads a map, it registers this map with its file descriptor into this global structure and then new Bpf probes as they get loaded, they'll look up to see if they already have a map and then just reuse the file descriptor. So we end up sharing the map amongst multiple probes without needing to use the Bpf file system.
Does it make sense.
Tyler Yahn 00:20:13 That makes sense. How do you disentangle the telemetry that comes through the map, though, and associate it back to like the probe?
Is that just.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:22 Thank you.
Tyler Yahn 00:20:22 Structure of the data.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:24 Yeah. So everybody ships data on the same sort of ring buffer, if you will, for us as a ring buffer. I know Gowater uses a perf butter buffer that this shouldn't be no problem for us switching to a perf buffer. I mean, we use a ring buffer, because apparently it's faster, but but it does come with a kernel restriction, so you can't use all the kernels because of that.
So the way that these events get pushed on to the ring buffer. Now, each event contains a process id.
so that we know for which process this event is for which is the multi-process support, and each event contains a type and the type and based, when it comes through, gets to sit decided to as what handler should handle it. So it's sort of a requirement. So if you look what I had to do to this data structure that's currently in in go auto.
So yeah, I didn't mean to do that.
Think I put it in. I think I have to go in common.
Alright, do. I don't have the file open anymore.
Tyler Yahn 00:21:44 In go auto or in in
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:46 It'll be. This is my sort of like a hackathon branch.
Yeah, yeah, yeah.
yeah. It may not be all nice and clean, and whatever. But I want to show you the auto span data structure that I had to sort of massage into making something work.
alright. So the the auto data structure in auto span looks much nicer. You asked me in go auto, but there's certain restrictions that we have to go through to make it work with Ob.
So the 1st one has to have this type, which I think is similar.
that shouldn't be different. Yeah. So there's a kind I don't know why it says this, but whatever and but the the difference is that we have this pit info. That's a requirement, because otherwise we don't know for which process this event was generated.
Tyler Yahn 00:22:50 Yeah, that makes sense. Okay?
And I'm guessing. Back in like ghost space, you're keeping a map of of like Pid to like information about the Pid. So like, yeah, instrumentation library and that kind of stuff.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:02 Yes, so so this is the sort of like a service registry that we keep around, which has different kinds of attributes. So it has attributes about the executable we call this service attributes.
So his attributes about the executable, and that data will eventually get enriched. If you're running into a system that has Kubernetes, for example.
in the future, can be extended for like cloud vendors and whatnot, so that service map kind of sits there. And then initially, we start with just the executable, we discover the executables. And then we based on the container ids, we try to look up at a higher level concept.
And the main reason that's done is that to not require people to set up hotel service name, for example.
similar to what the operator would do automatically. If you haven't set it, it will try to do it for you right? It uses the same algorithm, the exact same one as the auto operator and the ultra collector. So we are compatible.
and the other thing, this is sort of like a minor thing may not be required in general.
So Raphael did a little bit of a surgery of how we parsed.
Maybe he can speak to this if you fail, if you like, about how we parse the the Ebpf. Events coming from the ring buffer.
Mainly we like we found at some point there was a user that opened like a.
you know, like an issue in bail. A while back. And I think it's a community user that's been pushing the same community user that's been pushing for integration with Ob and the collector So they found that a lot of the overhead they instrumented, like, I think, like thousands of services or something, and the main overhead was parsing CPU wise parsing the events from the ring buffer because it uses this. The Evpf Go library uses this reflection mechanism.
So then, if I looked into this, and if we sort of don't use pack data structures and pad everything correctly to a bite to a boundary of 64, we're able to just cast events. So no reflection and sort of looks ugly in the code. But it is much faster, like orders of magnitude faster eliminates the overhead, which is another reason why this looks as ugly as this. So if you look over here.
this is the probe code.
Sorry. What?
Trying to find my data structures.
Rafael Roquetto 00:25:55 I can. I can add a little bit of of quick context.
So basically, there were 2 major bottle bottlenecks. One was copy, and there was a lot of. So we we received the event, and then, once we receive the event we were parsing using. Yes, buffers of buffer of read, or something like that.
I don't remember from the top of my mind, but using the usual like binary parsing Api from go, as Nicola pointed out, that on itself, once it's it has, it needs to copy that from a ring buffer. And there's a lot of intermediate copies happening there.
And that was 1 1 of the issues. And then there's a lot of heap allocation as a result of that, because of creating slices and whatnot. So there's a lot of copies happening that was like big overhead. And then there is the reflection part that Nicolas Nicola mentioned as well that it would look at. Look at the target struct because you pass that pointer to a target struct where you want to serialize it into or deserialize it into, and that itself. There's a lot happening there for reflection. So it just took a more like traditional approach. Where?
look at the ring buffer. There's 0 copy happening now. It just like Re, interpret the the bytes as as the struct like you would do in, you know, co c plus plus.
And and you you put you use that until you you convert into your final. There's gonna be one copy at least. When you go from the ring buffer to an actual structure sharing. But you get rid of all this intermediate intermediate bullshit that that's that was happening. So that was it. And the packing that we had to remove was actually I mean, not performance based. Although it's it's nice now that everything is aligned. But because the Bpf to go cannot generate back structs. So we still rely on the structure types.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:59 Yeah.
Rafael Roquetto 00:28:00 You have to go, but you all always add padding. So it's so it was like, Okay, get let's get rid of padding and and just compile with the tool. So that was it? Sorry?
There you are.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:11 Yeah. Yeah. So a lot of those checks that were done at Runtime to see the type doesn't match. Now they're done at compile time the generator will freak out if things are not aligned, and if your data structures are not like multiples of the 64 bits.
but you. So, for example, a struct like this would not be able. We will not be able to use this. I had to remove it.
and then I had to sprinkle this padding at the right places, which is not not optimal. I've been modifying this data structure. Probably there's a better way to kind of reorder the fields to have less padding. But yeah.
Rafael Roquetto 00:28:51 We have.
Tyler Yahn 00:28:53 Do you choose the target struct though like, how do you know that the target struct coming from the ring buffer is the one that you're you're looking for.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:00 Right? So this comes this type thing. The type thing gets populated with the event kind that. It must be the 1st thing, so I'll show you how this looks in the actual parser if you like.
Tyler Yahn 00:29:17 No, that that makes sense to me. I get it. I, yeah, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:21 So it reads, the 1st bite does this, and then it says, Okay, based on this, it's this kind. Let me serialize it now as this this thing.
Tyler Yahn 00:29:38 Yeah, we do that in a few other places in go auto as well for.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:42 Tribes, too.
Tyler Yahn 00:29:43 Yeah, yeah, for the types. Yeah, yeah.
Rafael Roquetto 00:29:44 I just wanted to point out that actually, there's more than one copy happening still, because I remember now ceiling to read from the ring buffer and go it will when you do like ring buffer read it reads some ring buffer record struct and that's 1 copy that they do, and there's nothing we can do about that. But that's fine. I mean, just so, you guys know. I said 0 copy before. But no, there's.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:15 Yeah, so this is how this gets done. Now, without reading on the ring buffer, we just put the raw sample for the ring buffer. And this this is now called from just like you would imagine. So we read, one type. And then we switch on the type and based on what it is. We just go. And okay.
Tyler Yahn 00:30:42 Yep.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:43 Yeah. And then we call the various parsers.
Yeah. So I think some things that we can.
the sharing of the data structures without. I think that's an easy one. If it's acceptable to be moved to go auto that would enable us to actually do this.
Like it will be for no reason now, and there was a reason in the past.
I suppose, that we kind of to reduce the overhead. We kind of put everything into a same probe if you will. So there's a goal probe that tries to try all of them rather than there's structured probes that detect things.
But we can move away from that design. We used to have them split.
We before we knew or before Raphael invented this sharing of the maps. We were struggling with permissions required at certain customers. So then we kind of collapse everything into a single tracer to avoid. At least, if you just go shop, then you don't have to use the the Ebpf file system to share maps. But then that's sort of like no longer requirement, because we do have the ability to now share maps with this this approach so we could use different probes.
But we have to figure out a way how we could potentially make Constance work. That's the main challenge.
Think the rest should have been.
Tyler Yahn 00:32:25 I think the Constance is a little bit I think it's a little I mean, I don't know the actual steel thread portion. If we're talking that way yet. But like.
Like if we wanted to like. We have like what Mike is working on right now is you pass configuration through like this probe in interface, right? Like it doesn't seem like you couldn't pass in some sort of like declarative thing that says like, here is the the map struck to go look up an offset in right like that seems totally viable to me. Does that not seem reasonable?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:57 No, it does seem reasonable.
yeah, we're like a fast enough function custom provider for how you're going to initialize your constants. And then we do something there. That would work. I just don't know how we're gonna do this. This is what I'm struggling with right now. I'm not sure. There, I'm not saying there's no solution. I'm just saying like, I'm struggling to understand, like how even myself, how do I make this work?
Tyler Yahn 00:33:24 Well, I also think I think that, like this may be something that the auto insertation could adopt as well, because, like, there's not much overhead in this, in this looking up this map right for this offset, because it's done once at the beginning of the process. And so.
Mike Dame 00:33:38 What's.
Tyler Yahn 00:33:38 Passing in. Yeah, go ahead, Mike. Sorry.
Mike Dame 00:33:41 If I can. Just this was, this is really great to see, and I think a lot of it kind of overlaps with what I was trying to talk about in there to in that pr, so if I can just take it to a little bit of a higher level and talk about what you know, the issues that you've pointed out how they relate to what I'm doing.
the so the overall design that I'm trying to propose really consists of, I guess. 3 parts where 1st is the probe Api itself? Which is where you have, like your hotel. SDK probe here. It's the like, Tyler, said the config that could be accepted.
so. But it's also very declarative and not very functional in that it'll say these are the symbols that I want. These are the offsets that I need. And you, you know you could write that probe, rewrite it, wrap it, however, you need to, if you need to customize stuff in it, but for the most part it's a dropable standard module with that's really only defined by an interface that's then implemented by either a base type or a type that you've implemented. That's the probe. And what I'm trying to do, at least in this pr, right now is shift the functionality. So things like loading and closing and managing. Really, the probe lifecycle into more of the the framework, or you know the manager that we have. That's where I'm thinking. Things like, you know, this offsets table.
Stuff like that would be easily extended. And when every time that you've mentioned through here like is this something that you know, we would contribute back up to go auto. That's exactly the idea that I'm having to is that things like that like absolutely we should be, you know, functionality, even though, like improvements on, you know the efficiency, you know, for, you know.
probing events, I think that's something that like the span struct itself, handling spans that should be going through, I think. Go auto and the library there, not so much in the probes themselves. And so that that's the second part of this, the 3rd part component is then Obi, or or Otigos, or bela, or whoever's importing these things, what is reasonable to import and what's usable for you. So if, for example, in this Pr that I'm doing if I got rid of the probe dot load function.
that's the kind of input that I'm wondering from. You know the Ob project right now, would you end up using, you know, calling new instrumentation, getting a manager and being comfortable with you know, adopting that and loading probes through the manager? Or is that something that's breaking? And you prefer to be able to call, you know, probe dot load rather than you know, manager, dot load, probe, and pass it a probe like that.
Rafael Roquetto 00:36:44 Sorry, just to add some context, because I saw the Pr. For people who are used to pay the slash ob code.
The probe would be analogous to to our tracer.
Yeah.
and the managers and others to the instrument, or you know the things that contain you probe K. Probes methods. That does that. Yeah.
Mike Dame 00:37:05 Yeah. Thanks. Raphael.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:08 Yeah, I think we're okay with probe load for now. I'm just trying to understand. I think we need to tap into that level because of this maps rewiring unless we move that code over as well.
Because the way we do it was we now load the Bpf.
Directly, and then we rewire the maps. I can show you that code that's sort of critical for us to get, because these parts of the I like go auto does the same thing. Sort of. There is a map that's shared like. If you set up a context of a parent in Htp.
and then you do a SQL. Statement, you're able to pull and connect the dots between the 2 right? So or same, for, like an outgoing request, so which means the Http client probe is reusing data with the Http server probe and so those maps that are shared. So if we we need move that code, then maybe we can use the manager, but I can show you how that's done. I think it says through Mentor.
Mike Dame 00:38:20 Yeah. And I guess that that's a good way to frame it to that analogy between instrumenter and managers that we don't wanna duplicate. You know that there's a manager that exists and go auto and an instrument, or that exists in ob it would, you know, should really just be one of them somewhere, and if the instrumentor is something that wraps the manager and then adds multiprocess or other things that you guys do on top of it, then that's good. But we don't want it to be reproducing exact behavior that the manager has. And if that's the case, then maybe instrument, or just exists in ob, and that then we get rid of manager, or vice versa. I'm pushing for the vice versa where manager exists and ob wraps it. But that's what I'm trying to understand that I'm obviously coming from a bias, too.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:08 Yeah, so this is the piece that's sort of critical for us, like Tracer is a probe in the world of Go auto. And this load and assign. So we load the spec of the tracer directly, and then, after that we do this resolve maps which rewires the file descriptors to be able to share the maps without the Bpf file system, and then eventually does this load and assign so that if that becomes part of a manager that we can reuse somehow. Then, definitely, we can share that level. But otherwise we would need the probe somehow to fit into this way around.
Rafael Roquetto 00:39:48 I think I think you'll be cool if this became part of the manager, and I think if you want, I mean Mike can speak to it, because it's fresh in his mind. But this is a still specific case, but we maybe can cater for that on the manager, or we can simply add some sort of generic hook for this particular use case where you need to kind of pre-process the collection spec before passing into the loading program. So I don't know. I'm not saying this is a good idea. I'm just a brainstorming like you can. Just maybe I don't know how we would fit on the Api if you would feed on the manager Api, that you could just pass like a function to it. They say, hey? Call this function. Call this hook whenever you're loading like a collection spec, and then downstream projects like Ob or Bela could just provide their own custom things that implements these, for instance, and it's also future proof.
And then you can add convenience convenience, functionality like, for internal, for instance, things like that where you can. If it's a a widely used or required use case, you can also bake this into the manager. So people don't have to necessarily bother with accessing these hooks, you know, explicitly for 90% of the cases. And they just there. For you know, the the corner cases that we haven't thought of I don't know just thinking out loud.
Mike Dame 00:41:18 Yeah.
I think my idea, my whole thinking with this was that the manager in Go auto would be the extendable contributable we can evolve it and change it. Whereas that the probe Api itself being more of the you know, this is v. 1. It's an interface. It's not going to be broken unless there's a v 2 but it's we don't need to cross that bridge yet. But that being the fixed, you know, it's the standard it can drop into any component that is implementing this library.
Whether it's using the manager or writing its own thing, we prefer the manager, I guess. But yeah, the manager being the thing where, if we need more functionality, let's add hooks into that. And then that's the really the framework of the SDK for loading and unloading and configuring go probes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:14 Okay, cool. Yeah. So I think we, I think we'll make it work like if we started off with. So this I think I see 2 critical components that we need to kind of contribute to go auto to be able to leverage it. One is the multiprocess support.
Obviously, this also map. I just remember this. We use this everywhere. It may be an overkill. I know people will call me paranoid. But typically when you use like something like a go routine or a pointer.
That works for a single executable right? Because the pointer is unique for a given go program.
But then you'll load multiple executables. And technically, something can come and go. And I mean, when you have a virtual address, space is not a problem. But imagine we had this I mean theoretical scenario which has sparked the paranoia is that for executables that come and go so technically, you could have a process that restarts and then reuses an address that you have a pointer to. So everywhere we use this, go, add, or key.
When we actually have a an address in the go heap.
We wrap it in this. That contains the process. Id.
That's we never hid this case in production, but it was theoretical. So we decided to do it.
Again, it's I think it's not that big of a deal.
but it would require that some the maps that are shared for the programs, we slowly start to migrate them for using this office table and then wrapping the addresses with Pid. Essentially.
Tyler Yahn 00:44:16 Yeah, I don't think there's any problem with any of that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:18 Now.
Tyler Yahn 00:44:19 Honestly, because, like I, I think that that all seems to make sense, it's all at a very low level, and it all is very abstracted by the time you get up to the new instrumentation. So like, I don't think if there's any problem with that.
I do wonder I've got 2 questions of of like, how how we plan to like drive this. So one is is in getting the data like parsed and getting it.
getting it to the user right? Like, eventually, like you started in this Epf space. And there's like some sort of telemetry. And it needs to get like processed and shipped right right now we're doing that via a map in in a particular way here in Ob, and then we're doing it with another. I'm sorry. Not a map, but a ring buffer, and then we're doing it with the perf buffer in in auto station, like.
I don't think that I'm not too concerned about the ring versus the perfuff or thing, but just more about like so the manager is the thing that's going to be processing, or the instrumentor is the thing that's going to be processing these events right? Like, yeah, that needs to get, I think, unified.
And it kind of comes back to this second question I have as to like, what if I have like a 3rd party.
probe that I want to integrate into this like? Can we do that like. Obviously, we can enforce some sort of like.
you know, restrictions on this, like in Raphael's like hooks, would be very helpful in extending capability here. But like, let's just say that I have, like, you know, some Joe Schmo Company, and I have my own application, and I want to run some sort of probe for that, and I'm happy bundling everything, and I'm happy like taking that probe.
compiling into a binary and then running that myself. But just like, how do I get that code integrated here like, do I have to fork ob? Do I have to fork auto instrumentation like, can I? Can I just provide this probe Api, that Mike's coming up with like.
you know, what kind of restrictions do we have to put on that that like? Obviously, they need to use like an offset table. They need to talk to the same like, do they? Do they need to talk to the same perf buffer or like.
Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:24 No, they can have their own, I mean, I think I mean, we do have couple of separate ring buffers that are used by different excuse. For example, the watcher and the debug logger. Those guys use
Tyler Yahn 00:46:42 It's more just like, how do I? How do I get the telemetry from that probe into the into the processing pipeline?
Because I think that's why I'm asking, yeah, go ahead.
Rafael Roquetto 00:46:52 Think in very generic terms, and Mike can correct me if I'm wrong, like, when you're loading stuff. So probe the probe is loading a bunch of Evpf stuff maps, programs and buffers, pair of buffers being buffers.
And it's going to. I'm hoping it's going to provide a number for the top of my mind way for the user space to tap into things that are tappable by user space. So the ring buffers and buffers being 2 of those entities. I think the manager wouldn't necessarily in my correct if I'm wrong, if that's not the way you're you're planning it. But the man the way I I think of it is that the manager wouldn't make wouldn't make any kind of decision, or or or semantics about those things. It's just say I'm loading this thing. This thing comes with a perf buffer.
and then whoever is using the manager knows that it's loading like it passed the probe to the to the manager, manage, load this probe, and so whoever the calling code also knows that the probe comes with a perf buffer, that later I will pull or tell the manager to pull, or something like that. I think that's how it personally should work, because then it becomes very generic. I don't know, Mike. Well.
Mike Dame 00:48:05 I I think that you are right, and I think that Tyler's got a really good point about how do we link that into because the manager provides the you know the span processor and exporter, and that's where these events get converted. That's kind of the shared link between these maps and the like the manager, go auto evpf framework where Raphael, what you're saying like, exactly. If if a user like Joe Schmo Company wants to write their own probe module they define their own maps, or whatever they want to store like. They want to track probes for this event. Http. Events, or like my library events, or whatever that's your own map. But at a certain point there are there's the context. Propagation between, you know. Go routine that needs to link into these types. And so those need to be at least defined in an Api somewhere, or someone can say, like, you know, Midwe provide also the the C library for working with it. We basically have a whole C library of helpers and structs. So that, I think, is a big part of this and then the output of the the spans. Those need to be in a type that the machinery that you're working with understands. And so you could implement that your own. You know, you could have your own manager. Maybe someone wants something completely, you know, different and crazy. But I I think.
for the context of this argument here. That's where we need to link in is structures of that we're providing as part of like the, you know, probe library, and this is the probe Api and go. But we also have that C probe library that is, I think, kind of its own beast and you know.
cleaning that up and shipping it can be its own project. But this is where it ties into. How are we? You know, what's the decision gonna be? How does that link in? If someone's writing their own probes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:05 Yeah, another thing to consider is So one thing that that I it's interesting because they, when the events come from most of the interfaces that we have in go auto.
They grow directly into this b-tray span, slice right.
Tyler Yahn 00:50:26 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:27 So we construct the span straight out there and sort of like it's done differently. No, be. I don't know if it's there's a way that we can kind of resolve. That is there a way that we can get the function to? We provide our own process for that probe. So the reason I'm saying that is that I mean, maybe this is the wrong approach that we're taking as well. I just want to point out but it. So expanse does make sense for go auto, because it's purely tracing infrastructure. Right? So what else is there?
We're just going to put the traces. And that's it. So, for example, if we take a look at.
let's say, server, request we we do this span slice, and we we create this event, and we push it along right? So the question is like with Ob being also metric.
So we do all this machinery around modifying the data structures as they come through.
So you have this event. But maybe you don't even want traces. So you're just purely producing metrics, in which case, you know, the roots are important.
So here we have a URL pad, but no URL root.
The span name itself. We need a we need a we need a name that's low cardinality. So he needs to go through these processors that try to like. Look at the rules set up for the roots and say, Do I match to some of these definitions by the end user? Or do I have to apply the heuristic and try to automatically determine a low cardinality path, a euro path right?
so we would much rather prefer to get the raw event and do what we would do with it today. But we can consider that as well.
going forward for something like the go the the SDK instrumentation. It doesn't make sense, because that's purely for tracing But if you look, what we typically do is we? I mean, I'm not saying, this is a great design. It's just how we do it. We have this God data structure span.
which where we fill out information and that gets pushed through the pipeline and gets enriched.
For example, this span data structure will get attached a service thing.
At some point and then it will like if there's like a path set up like the Http path used by the by the Api. Then somewhere along the line there's a root processor. We'll try to make a low cardinality Http route out of that and generate the trace span and so on.
Tyler Yahn 00:53:43 Yeah, that's a good question. So we originally.
So we converted to this P data structure, because ultimately we wanted to like speak that. And we wanted the least amount of transforms as possible.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:56 Conversions. Yeah, it makes sense.
Tyler Yahn 00:53:58 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:02 I mean, it's directly consumable by us as well for the tracer output for the tracing output. So traces also produced like for us, we go with all these spans all the way to the end, and then and then we convert them to P data as well where you could think about it. One.
Tyler Yahn 00:54:22 Yeah, we.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:23 Sort of challenge there is that we like again, this is not a problem in go order, because it's single process.
but for us it's difficult as well, because we don't want to duplicate the resource attributes.
So now you have to create a span. They declare the resource attributes, and you list. The spans that contain this right when you push out the traces. So.
But we don't like, since we're getting events from all the different processes as the events come through on the rain buffer. We sort of like batch, process them, and like here, and produce like, figure out what service they belong to. And then we batch them and then create a resource, and then.
Tyler Yahn 00:55:09 So that's I. I'm also realizing we got 5 min left. So I I think.
yeah, like, yeah, we got 5 min left, and that topic's probably its own hour. Long discussion. But so I I don't. I don't think Personally, I'm not opposed to like reevaluating the data model, like, I think it was just mostly for that transform optimization that we wanted to go in that direction. But I also think we put a pause on that because of like, we want to make sure this is like fully integrated with Ob at this point. So if that needs to change, I think that it's it's we should. We should evaluate that like you said, like, maybe it's not the most optimal in ob either, but like maybe we should, you know, think through like what we want there?
Because we also have the possibility to do these intermediate steps right like, if we're going back to like that custom probe thing like just speaking kind of like. There may be 2 points that you can plug in right. Maybe your probe can give like this internal data model representation. That is very like.
very minimal, and it can pass it through the ob processing pipeline to try to do all these path recognition all these other things, or it can just give you back this Otlp, right? Like, maybe it can just do its own processing. The thing is is, though, that, like one of the points that you did make out is that like you do batch processing, which is something that, like we are, you know having problems with on the downstream Otlp side like, if you're just passing single spans, how do you batch those together like? Because the collector doesn't do that because it batches at a resource level, right? And so that's yeah. That's a little bit of a challenge as well. So like, there's like, I'm saying, like, I think there's a lot of open questions that you're you're bringing up But just to kind of wrap it up as we're coming up to time. I think that like we've got a lot of discussion. I kind of want to watch this recording, because I think there's a lot here. And I think we talked about a lot about the probe. The downstream data model, I think, is another great discussion. Maybe we can try to put that on the agenda for next week. But yeah, I think I think I got a lot of ideas here interested to hear. Like Mike, it probably sounds as well like you probably got a lot of ideas like we got a lot more information about how to evolve right.
Mike Dame 00:57:16 Yeah, this was great. I'm itching to. I want to make this issue that I was talking about. I got a lot of good notes. I've been scratching down notes while we were talking. I think 2 key things that I got out, or I guess one was just trying to unify the concepts of tracer and probe and instrumenter and manager. I think that that is a big, that's kind of the big question that I came in wondering was because from our what we were talking about on the Sig yesterday, for people that weren't there was about, you know, how does that manager relate to ob. And then that discussion leads to. Well, what does the probe Api need to do if we're going to try to finalize that because that's kind of the like kernel of the the whole project is being able to define these probes. And then from there I took a bunch of notes on you know the issues that Nicola, that you said you hit trying to do the the auto SDK, there's things like structuring the spans, handling the multi process and the map sharing. That offsets that shared offsets. Map that you had.
I'll try to summarize all of that and you know we can go forward with. You know what's.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:24 And yeah.
Mike Dame 00:58:25 Yeah, project plan for yeah, I think I think, from my side, trying to unify the like instrumental to the manager and the tracer. Well, the instrument to the manager, I think, is maybe our our central thing to look into here, because a lot of that functionality, we said, could go through that. So. But we can talk about that offline and in the thread, and if I misunderstood anything or we, you know we can always correct me there. But I'll write that all up. I'll put it in the hotel Evpf. Instrumentation repo because I think that's probably where it should live right now. So yeah, we can work on that.
Tyler Yahn 00:58:59 Awesome only one more request, Nicola. I don't know. If, like you're able to share your branch. I'd love to poke around, if possible.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:07 Public. It's public.
Tyler Yahn 00:59:08 Oh, okay. Perfect.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:09 I'll put in the notes. Yeah.
it's in my ob repo yeah, I'll put it in the notes there. Share the branch.
Yeah.
it's slightly different. I I like, we try to avoid the Bps pro rights users. So I didn't want to change that. So I'm looking. It's a hack of the week. So yeah, yeah.
I'm looking at the I'm looking at detecting go interfaces and comparing that. So I can parse you know how you guys do that?
When when the when the flag is set, you go in and you kind of try to trigger the tracer, start a different type so that you can get set attributes to be a straight up call.
And I was. I didn't want to set that. We provide users. So I'm saying, can I find the attributes as they're passed in
Tyler Yahn 01:00:02 So.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:02 I think I have a way, but it's a hack of 2 weeks, so I mean I can do my hacking.
Tyler Yahn 01:00:09 Yeah, I'm interested. So yeah, I I guess just I'm not not expecting production code at all. So just in more curious.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:16 Alright! Alright, no, absolutely yeah.
Tyler Yahn 01:00:18 Alright. Well, cool. We're at the end of the hour. Want to be respectful. People's time. Thanks everyone for joining. Appreciate it. Obviously, continue the session slack, and then next week yeah, we'll we'll hopefully continue this discussion. So appreciate it. Bye, everyone.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:30 Alright, bye.
