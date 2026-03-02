SIG: Collector SIG
Date: 2025-06-18
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 02:24 Hello!
**Christos Markou** 02:28 Hey!
**Andrzej Stencel** 03:12 Right. So let me read out this thing that Pablo added.
there's a document for the roadmap and achievements of the collector Sig.
that will be shared with the Technical Committee and the Governance Committee.
So if you have any comments out there, because before end of week, I suppose that is.
and, Roger, you're next.
**Roger Coll** 03:41 Screen. So also the same issue.
**Christos Markou** 03:47 Wait, cannot hear you, Roger.
**Vihas Makwana** 03:50 Yeah.
**Christos Markou** 03:52 Now we can.
Now it's okay, I think.
No, it's not.
**Roger Coll** 04:15 Does it work now? If not.
let's, I will be the last one.
**Christos Markou** 04:20 It works, it works. Now.
**Roger Coll** 04:21 It works. Okay.
So I hope I'm sharing also the hotel collector issue. And
basically the let's say, the context of this issue is that in the collector, right, we have the the concept of components, and those components are started and stopped by the internal graphs. Right? And those components are normally the ones defined in the
configuration.
But then we have some of these components that are dynamically, for example, spawning other components, and and that is the case. For example, as I put here of the receiver Creator, right, the receiver Creator, based on annotations or auto discovery, let's say, on runtime, it can start components or or stop them.
And
the issue is that for, let's say, the root issue of of this is that we don't have observability of those dynamic components we in the. If you look at the, for example, if you are monitoring the health check extension endpoint, you won't see. Let's say, the yeah, the components started by the receiver creator.
So you will know if there's a if if it has been started, stop it, or even if there's a a fatal error. And
in this issue here I'm trying to define. Let's say a term that it's not yet in the hotel collector, but somehow a way to identify this. These components, these components launched by other components.
but also it could apply to other. Let's say.
other units of work. For example in the you know, there's some receivers that maybe have different scrapers, that they are not related one to each other. That is the case. For example, the host metric receiver that you have the
CPU, the process scraper, the you know, the memory and and and others. And now I think we are adding nfs, and each of those scrapers. They are not related to each other, and maybe one can fail and the other can continue to work right because of a permissions issue or whatever.
And the issue here is that we don't have observability for this sub components. Neither. We don't know if well, you need to check the logs, but you don't know from, let's say, from an events perspective. If the CPU is scraper is working, or or it doesn't.
So in this issue here, I'm trying to define this sub components concept and then just defining
the issues that we have with the health check that they are not seen anywhere there.
And why I wanted to bring here is just I I researched a little solution that it would be, let's say, adding this new sub components id into the event structure in the component status package.
And just this new function. And with that, let's say that the root components should be able to provide status updates for any subcomponents that they wish.
And this solution, let's say that it's not breaking changes. It doesn't change coronum
let's say Apis, and also for the sales check extension. It would be quite straightforward to
to just show up. Let's say these soup components because it's a.
it's a recursive structure at at the moment. And yeah, just wanted to bring here. If there's like opinions, or or this has been raised in the past already, or
other solutions. And
yeah, I I will leave it up up to you, or or if you want to put a comment into the issue.
**Jade Guiton** 08:32 Would it be possible to make this more generic? Add a component id sorry, a component id field to all
events.
But we don't have to treat root components and subcomponents differently.
**Roger Coll** 08:50 Yeah, the thing is that I don't know if I hear the.
And
we don't have the link. But let's say that once the graph initiates, this initiates the component, it embeds a private component, id.
let's say, on the structure. So and then basically, the the component when wants to send events. It doesn't know about its Iv, and just let's say, sense events in in that way.
So in that sense the components can. There's not a way to now nowadays to generate components. Id.
Then.
**Mikołaj Świątek** 09:36 You would have to be able to expect to inspect it right? You'd you'd have you'd have a split where you might. You might get status status objects from a component which doesn't have it set. And then the core framework would have to set it right if you added it that way if you want it to be consistent.
which is a bigger change, or or it's a big breaking change where everybody would have to, you know, would all the components would have to start to maintain the status differently?
even.
**Jade Guiton** 10:10 I'm thinking, is that we can keep the assignment of the component id external
and we have either the core collector framework
set the component Id for root components, we don't have to change the Api, so the component doesn't have to know its own Id.
and for components that embed subcomponents, then they can use the exact same function to assign the component Id to events that maybe that could be a way of doing it.
**Evan Bradley** 10:46 I think I'm repeating. A variation of what Jad is saying here. But I know in OP. Amp we've made the concept of a component recursive.
So a component can contain other components rather than strictly saying that they're subcomponents. And so I would, without looking into this too much more. Or really, having looked at component status reporting closely in a little while.
I would also suggest that we simply make it so that components can create their own components.
**Mikołaj Świątek** 11:21 So basically want to move, move, what health check v. 2 currently has, or or the status report, or the or move aggregate status into in into car. Essentially right.
is what you're saying.
**Evan Bradley** 11:41 I think it would make sense to move some level of aggregation into core.
I think we'd want to pay attention to exactly I mean, part of aggregation is
you know what your assumptions are for, if
you know, if you have a set of 5 components and they're all reporting different statuses. What? What is the top level status that you report?
I I don't know how much we want that to be customizable. But,
broadly speaking, I think it does make sense to
standardize on that a little bit.
**Roger Coll** 12:21 Okay? So if I understood correctly, kind of as a new Api on the core collector to create, let's say,
soup components, id from a given component of current component id
and then use that to embed it on the events and and so on.
instead of free freely creating subcomponents. Id
alright, so there's no more comments. Well, please leave any in the in the issue of jade.
**Jade Guiton** 13:09 I was just wondering, regarding what Evan said. If you have multiple subcomponents
with this new interface, how would you report that? Would that be like a
a separate issue being able to report multiple events?
Or is that part of what you're
you're thinking of working on here.
**Roger Coll** 13:30 My idea would be just.
let's say, not not aggregate them in in a, in a.
in multiple events. But just send, let's say
each of components one by one, not
let's say aggregated in in one piece.
**Jade Guiton** 13:49 Right. It's just that. I don't fully understand how report status works. I haven't really looked at the Api, but I assume it's called only once for top level component, right?
**Mikołaj Świątek** 14:01 A component and components call the Api. So it's up to them what they want to do.
**Jade Guiton** 14:06 I see in that case that makes sense.
**Roger Coll** 14:09 Exactly. Yeah, cool.
Thank you.
**Andrzej Stencel** 14:31 Yeah. Then.
**Yaten Dhingra** 14:33 Oh, yeah. Oh, Hi, folks, I am a new contributor here.
so it can be. Just I was working on an issue over open telemetry like, it's a good 1st issue. So if we have time right now, can we just discuss about it just for 2 min.
**Andrzej Stencel** 14:49 We have a agenda this, Doc. Let me put it on the chat. You can add yourself to the agenda.
Okay? And.
**Yaten Dhingra** 15:00 Okay, okay, okay, got it.
**Andrzej Stencel** 15:02 So Shimon. Sorry, Simon Simon.
**Simon Olander (SAP)** 15:06 Yes, that's me. Thank you. Simon. I'll share my screen right? So this is annoying. Okay.
that's right.
There we go. Share.
Oh, that's annoying. Okay, I need to restart zoom, of course, because that's what happens when you don't have permission sets okay back in a sec. Maybe take another one in in between.
**Andrzej Stencel** 15:33 Okay? Sure.
Mattelston.
Yeah. Let me try if I have permission set.
**MU Mateusz Urbanek** 15:41 Man, hey?
Okay, so can you see my screen
cool? And so I don't know if this is correct to discuss it or correct meeting. But
I raised a poor request and issue about adding new architecture, tuple for the collector.
For all some of the releases it's targeting. Linux risk v. 64.
And it should just work fine. I've been able to build that manually. I have.
There is a board going to my to my home right now, so I will be able to test it on the live system in next few days. However, I would like to know a little bit more. What is the process of actually adding a tier? 3 support to to the collector?
I have got a few of the initial reviews here. But, as a few people, you pointed out, I should just come and discuss this to more people just rather than just submit the issue. And Pr.
**Andrzej Stencel** 17:07 I mean, sure, if you're able to join the seek as you have today, then that's great. I see the on this pull request that you created and releases repository. There was a comment from Antoine telling you to create an issue in the collector core. Is that right? And you did that already as well.
**MU Mateusz Urbanek** 17:26 Yes, yes, I did that. There is issue, error.
**Andrzej Stencel** 17:32 Oh, we created an issue. Okay? Okay, okay, yeah. I mean, in general, I think it's great to have to to support the risk. 5 architecture, and we just need to like follow the process and do everything right. I haven't seen that yet, so I'll definitely take a closer look, and
anyone else have any comments on this.
**Mikołaj Świątek** 17:54 Do we have? Do we have requirements for for tier? 3 actually.
**MU Mateusz Urbanek** 18:00 The only requirement that is defined in the doc is that it builds
however, I am not able to trigger the the release on my own work, as it requires the pro license, so which I don't don't have, so I can't verify that it will work in Ci.
**Andrzej Stencel** 18:27 So we don't need a actual risk. 5 computer to build this right? Because we can cross compile and that's all we need for risk. Tier 3
**MU Mateusz Urbanek** 18:38 Yes.
**Andrzej Stencel** 18:39 Yeah.
Hmm.
**Mikołaj Świątek** 18:43 2.
**Andrzej Stencel** 18:44 No, it's fine to me.
**Mikołaj Świątek** 18:44 Seems seems reasonable. Yeah, I I this for this kind of thing. I think you actually need approvals from like a majority of core maintainers either way. But I think you've done
everything you needed to do. And now it's more of a question of waiting and and chasing people to to give their opinion, it would probably help if you also, I know which I know is a little bit annoying. But there's a the collectors alternate right. This one is from is for is for Emea, and next week is going to be for for NASA, which is typically
more attended because more maintainers are in that time zone. So if you could also come reschedule this for next week and and bring it up as well. Sorry sorry like this is a you're suffering from from like from a you know, internal hotel Sig. Meeting organization problems. But it would probably make things faster for you if you do that
as well.
**MU Mateusz Urbanek** 19:48 Yes, sure. Thank you very much.
**Andrzej Stencel** 19:54 Thanks. Simon.
**Simon Olander (SAP)** 19:56 Yeah. Now let's try again.
Alright. So I I just want to have some feedback really, on any component that I have an idea for and it's a bit of a half big solution. I would say.
can you see my screen? Yeah. Okay?
And I added this issue to describe some kind of file watch receiver. And the idea is that it's a receiver. Or maybe I'll start with the problem statement, basically for auditing purposes. It's quite nice to have an idea of what happens with files, so if they are created, renamed, deleted, or moved, whatever it could be besides. And things happens with files, and we want to maybe know about them when those actions are happening.
and send them to some kind of sink somewhere or downstream. And this is something that we don't have at the moment in hotel as a receiver, or any kind of component, from what I can tell.
so that's why I wanted to add something like this, I added, like a rough idea of
an offline here. I had to talk with you, I guess. Andre. Just.
That's why, yeah, and you also referenced it in a different issue as well. And we kind of talked about the similarities with the file log receiver.
So I guess my my kind of question is, you know, is this a sound idea to continue approaching forward like continue working towards, to have something like this. And then second would be like, how different would it be them from the file of receiver in essence? Right? Because
you you mentioned that as well, that it's quite similar, but also a bit different.
**Andrzej Stencel** 21:37 Yeah, exactly. I'm kind of leaning towards having this functionality as a separate receiver having a separate receivers comes with the problem that you need to have a sponsor for it, and somebody to get a sponsor because everyone's a bit overwhelmed.
But I do feel that it's it's really orthogonal to what file receiver does.
yeah, as long as.
**Jade Guiton** 22:07 So this watches files and emits. I guess events when they're modified. But does it transfer the contents of the file.
**Simon Olander (SAP)** 22:16 That's a follow up question. Right? Cause. I I would say that I have a bit of difficulties, seeing
in kind of I don't know an audit auditing purposes that you would also have this receiver sending the contents, because I feel that that's a bit of a different
I don't know it seems like a bit of a different problem, because then we'll have to ingest the file contents and send it away like in a way, if you already know, something happens with the file. You could maybe do it. But I also wonder if there's a way to simply
separate that as well somewhere else. Cause I'm not. I'm not sure if it's
how how relevant it is to send the contents of a big file or a small file. Really, whatever it is, simply if something edits to it.
And but
yeah, I I remember you talking about it a lot. And I'm sorry where basically said that, you know. Oh, no! It was this issue that I mentioned, maybe here the other one
where they talked about sending the contents as well
**Andrzej Stencel** 23:16 I'm a bit of a question mark. Actually on my side, as well, like if this is actually something that would make sense
yeah, these are, they seem related, but they are really 2 different things. I agree.
just sending the whole contents and just sending events about things happening. And your original proposal is about really sending only the events on what's going on with the file, not the contents. Right?
**Simon Olander (SAP)** 23:40 Yes, yes.
**Jade Guiton** 23:43 Right. I was thinking that it feels a lot more orthogonal to the file log receiver. If we're just sending the the events makes sense
us. Yeah, there's the question of
how suited Otlp is to sending the contents of entire files, or even diffs.
So yeah, it's probably easier to justify without the file contents. But
I guess the the question is like, Do we have like some kind of Mike?
We're saying this is for auditing purposes. But
Do we have references on what auditors might be looking for, and whether the file contents or file diffs would be important for this use case or not.
**Simon Olander (SAP)** 24:31 And I don't think I don't have anything on the top of my head at the moment.
The the thing that I could maybe refer to is that the the one of the feature gaps that we're looking at is like the one that the audit beats has a module log stash center module that does file integrity as well.
Maybe I need to double check that if it sends the contents. But that one is from my, how I'm using it is really for for kind of sending the events itself. Only not the contents. But I don't know. Maybe this is just also anecdotal right, my just my my view on it.
**Jade Guiton** 25:10 Right? Yeah, I guess it's just a
I wanna know. Like, if there's
if this is a use case that's generalizable.
**Simon Olander (SAP)** 25:20 Yeah, no sure sure makes sense.
But I don't know at the moment.
**Jade Guiton** 25:27 Okay, yeah, that's fair.
**Andrzej Stencel** 25:31 I I do feel that it's a valid use case just a matter of finding out. I would. I would definitely like to sponsor it if I had the capacity. But I'm
don't wanna sign up for something that I won't be able to fulfill.
I'm gonna look into it.
**Simon Olander (SAP)** 25:51 For for my from my understanding, sponsor means, in what sense is that the code efforts? Or is it the other stuff? Because, like I would be up for for
contributing with code efforts. Here I am not a member at the moment. This is the 1st member meeting I join, but I will be up for investing time into making happen.
and but I need to do the proper. I guess.
**Andrzej Stencel** 26:14 Yeah, sure. So you would be the like. The 1st code owner and the creator of the.
**Simon Olander (SAP)** 26:18 Next one.
**Andrzej Stencel** 26:19 Code. But you need someone who will review the the code. That's bad. And that would be the second code owner. And it needs to be an approver or a maintainer in the repository. That's it.
**Simon Olander (SAP)** 26:34 Okay. But then, next steps is to try to maybe try to figure that out. I guess
**Andrzej Stencel** 26:40 Yeah, maybe you could. I don't know. You could try to talk to Antoine and try to talk him into it, saying that maybe we could squeeze the file, sending the content sending into the as well. And I on my side, I will look into a possibility to find an a A sponsor.
Yeah, I will look into it. Don't wanna.
**Simon Olander (SAP)** 27:08 Okay, we can take it also, asynchronously, right? Like, in talking about it. So yeah.
cool. Yeah. Those all for me, I think. Then, unless there's other any other questions.
Cool. Thanks, thanks.
**Andrzej Stencel** 27:23 Thanks. Simon.
**Vihas Makwana** 27:25 I'll go next, I guess.
**Andrzej Stencel** 27:31 I mean, we have. Oh, yeah, yeah, because, yeah, sure.
**Vihas Makwana** 27:34 Yeah, yeah.
Okay. So mine is just an announcement for my Rfc. That I was working on since past few days.
So Tldr would be to simplify enabling statefulness for our collector.
Historically, file log used to do it like if if we had to. If we specified a storage extension. The file obviously would hook into the storage extension and enable statefulness automatically, but it was reverted due to some downsides.
So my Rfc. Tackles those, and
it it. It uses a converter to add a storage extension, and.
you know, enable the extension and enable the statefulness for receivers. Sorry
this this takes an example of file receiver. So I would request you guys to just go through. Go through this Rfc. And share your thoughts.
I think Andre has some idea around it. And we
we we have discussed this asynchronously, Nicola as well. So yeah,
that's yeah. That's that's not me.
**Andrzej Stencel** 28:41 Yeah. Oh, yeah, I like the idea of the stateful of having all the functionality in the converter. And you've created this Rfc. In the Collector Core Repository. If I understand correctly that the what needs to be changed in the collector core is to be able to like switch off or on a specific converter, which is already included into distro right.
**Vihas Makwana** 29:08 Yes, that's true. So we will. This will leave behind a feature gate if we decide to accept this Rfc. And and we and we might also add a command line flag. The feature gate would control the operatability of the command line flag and that would enable the statefulness.
Yeah.
**Andrzej Stencel** 29:27 Yeah, I think it's an interesting notion to be able to
switch on or off converters via cli flags.
I kind of think that might make sense.
So, yeah, oh, yeah, I wonder what other maintenance I think about.
I think that.
**Vihas Makwana** 29:57 I think that's it from my side. Unless anyone has any thoughts over this.
**Christos Markou** 30:02 I have a question.
**Vihas Makwana** 30:04 Yeah.
**Christos Markou** 30:05 Is this just for like simplifying the user experience? Is this the only value that this brings.
**Vihas Makwana** 30:14 Yeah, kind of yes, because let's say, if you have a.
you have multiple receivers that requested fullness, you you need to like manually add the
storage that storage field in the configurations for all of them.
So this kind of simplifies it for the user.
**Christos Markou** 30:34 Okay.
**Andrzej Stencel** 30:36 One. The thought I just had was, so you mentioned in this Rfc. Proposal the the change in the collector core that would need to be made to to switch on or off the statement of the converters. I wonder if it makes sense that, or maybe I missed it, that it's already done
to create a separate issue
just proposing that change. To be able to switch converters are on off in general. Would that make sense, you think.
like to be able to discuss it in, like in relation to that Rfc. But also in isolation from the concept of statefulness and unstatefulness. I think the the in general. The idea of having converters by being able to use them or not is interesting, and I wonder what that discussion would be.
**Vihas Makwana** 31:35 Dude.
**Andrzej Stencel** 31:37 Chad!
**Jade Guiton** 31:38 Yes, I'm wondering about the reason to use a converter for this. It seems like it could be
It seems like it could be difficult to identify the parts of the config where we
want to include this storage.
Key.
I.
It seems like it would be perhaps simpler to
introduce a concept of like a default storage extension.
**Vihas Makwana** 32:09 Hmm.
**Jade Guiton** 32:10 It would be loaded by the components themselves.
I don't know. I wanna I just wanna know, like, what is the reasoning for using a converter for this instead of
just introducing it at the code level.
**Vihas Makwana** 32:26 Okay. So one of the reasons to use a converter is well, in my 1st approach that I had shared with Andre. I used to manually go into the receivers and hook the extension, as you said.
but that had some issues like it wasn't possible to override that if the statefulness is enabled. So this converter it makes it possible for the user to override the default accession as well.
Oh.
that's 1 of the reasons that I switch to converter the other reason being that it kind of isolates all the things into a single place. We don't need to manually go inside every
every component and do it. We can specify a list of components that we want
state like stateful by default, and the converter would loop through the receivers and check for the
for the, for the components that that we require the storage extension and enable it.
So yeah, that that is the main intention behind using a converter.
**Andrzej Stencel** 33:22 If I may. 2 sense from my side. Yeah, I've worked on with vijas on this before. And
if he has a proposal of doing this in stateful as a converter and nothing else as
like, it's possible, because you can see the change set that because, like the
change that seems to work. That's 1 thing. And the the benefit of having this in a converter is that it's completely
isolated from any changes needed or not needed in the core or other in any components like the file of receiver. You don't need to change anything in the file receiver. You need to change anything in the collector core. You just need to add a converter to your distribution. And I think that's that's pretty nice in being able to switch it on and off this functionality is would be even better.
it's it's yeah what you said Jad, about maybe being able to do this differently. Yeah, I guess maybe it would.
Would it be better? I'm not sure
you said that. It's it's it seems to be difficult to done to be done in the stateful converter in a converter. Yeah, you have, you need to have like specific logic for every different component type. Probably currently, this proposal only has logic for file of receiver. But it's basically yeah, adding the storage field or or not.
And it's yeah, it. It doesn't seem that difficult.
**Jade Guiton** 35:00 Yeah, I don't think it's that difficult. It's just yeah. I guess you do need specific logic for each component, anyway. But I guess it can be outside of the component is the the nice thing I see.
**Vihas Makwana** 35:16 We go, live.
**Mikołaj Świątek** 35:19 Yeah. So some something that we also considered originally was to actually.
And I think there is an early issue in core to do this, to add an Api
to normalize the storage interface, because right now the fact that the storage interface to to set the storage on a component you. You set the storage key. That's right. Now, that's a convention. There isn't really anything in core that enforces you. And every time every component that wants to do. This has to do the the kind of song and dance where it loops over the extensions it fights the named extension, and then checks. If it's a storage extension, and so on.
and it's possible to move that all of that into a helper and have a config struct that lets you buy it. And in that case, if we structure the Api for that correctly, we would be able to to do something like, you know. Here we can return a default extension conditionally or not, depending on what set and collector, core
but that's a significant, significantly more amount of work and and like a new Api that you know, each component would then have to adopt. And and so far for us the converter approach is simpler, I think when we when we, when, when, if we decide to add the storage Api then, or the config storage helper, let's call it then we should consider that it that should have support for
1st for using defaults. But then, again, every component would actually have to adopt that separately, and they would all have to handle the case, that if you ask for a storage extension
you might get a default, or you might get nothing depending on on what happens, and then, appropriately, you know, appropriately deal with what it gets
that makes sense.
**Jade Guiton** 37:16 Yeah, that makes sense. Okay, so it's being considered. But yeah, it requires more changes and more adoption on the component level. So yeah, that makes sense.
**Mikołaj Świątek** 37:28 I think that if if there's like actual
significant use of this of the converter approach, then that's like a decent proof proof that that we should consider it in like a proper Api, I think, as well. But this is like a simply a simpler way of trialing. This idea of having a most more stateful collector.
**Jade Guiton** 37:52 Right? Yeah, like, I guess
problem with the converter idea is that you can't. If you make your own custom components, you can opt into it.
But yeah. So if if there's a lot of use, it would eventually make sense.
**Vihas Makwana** 38:16 Yeah. So if there are any things that you want to share, then just ping me on slack, or I'm under the Rf. And I'd be glad to
reply, so yeah, that's from me.
**Andrzej Stencel** 38:39 Yeah, 10.
**Yaten Dhingra** 38:42 Yeah, should I go next?
Yeah, just a second. I'll share my screen.
Yeah. So basically, I'm working on this pr for enhancement this enhancement. Pr, basically. So what I am doing here is like, I am adding the support for scope attributes for the Zip exporter.
So basically, currently, what it does is that it currently it doesn't contains this part. So basically, all the scopes are not included in the zipkin.
So I think, you, I think, someone commented on this issue, that this is similar to this function
and similar to this has to be implemented in the extract scope tab.
So yeah. And I think, some tests have to be added for to verify this.
So I'm just working on that I haven't pushed the changes for the test. So yeah, this was my update.
**Andrzej Stencel** 39:48 Yeah, this was great. Thanks, thanks a lot for doing this, and just add the test. And I'm gonna take a look and
we'll hope.
**Yaten Dhingra** 39:54 Yeah, yeah, sure.
**Andrzej Stencel** 39:55 Able to merge it soon.
Awesome. Thanks a lot.
**Yaten Dhingra** 39:58 This was my 1st year. Basically. So yeah, I'm a new contributor here, nice to meet you on.
**Andrzej Stencel** 40:05 Awesome. Thanks. Thanks a lot, Nathan.
**Yaten Dhingra** 40:08 Thank you.
**Jade Guiton** 40:09 By the way, there's an issue keeping track of the support of scope attributes across exporters and contrib I'm not sure if sipkin is currently in that
**Andrzej Stencel** 40:23 Yeah, I think that was this was born from that issue.
I think so.
**Jade Guiton** 40:30 Oh, yeah, okay, yeah, it's the the issue is linked. So yeah, I guess I'll
subscribe to the pr and update the list when it's merged.
**Andrzej Stencel** 40:42 Thanks, John
Douglas.
**Douglas Camata** 40:50 Sure. I just want to
call for some reviews on 2 Prs. That I have that
have been open since a while. Now I will start from the most simple one, which is, in fact, the second point
I have this Pr. That via a configuration allows the supervisor
to use a hub signal to restart the collector
to restart the collector node, to reload the the configuration of the collector. So, just as an alternative to stopping the process and starting again.
We could use this this configuration option to start to delegate more and more things to the collector itself.
I know that there. There is some interest in also
delegating all of the configuration merging in the in the future to the collector.
So this this could be could be a good complement for
for delegating more and more things to the collector itself.
I had some conversation in the in the sensors log
with someone I forgot exactly who now. So I'm sorry if you were here. But there were some questions regarding right. What happens if
you send the hub signal to the collector, and the configuration that you have there for it to reload
is bad in some way, and it will. It will cause the collector to crash.
and I don't think it will self heal
but that this is this is something
that we could could fix in a follow up, or I could even try to fix in this Pr. But maybe it might become a bit too big.
But we might need to implement there to. To add to this logic of when using the hub signal.
how to
how to ensure the rollout of the configuration is safe, right like, what do we do if the collector tries to read the config again, and the config is not good.
and there is even a good question. If
right, this should be probably part of the configuration reload logic in the collector right where it is listening for the Hub signal
and reloading the configuration when it gets it.
Maybe it doesn't belong in the Supervisor, because we would be doing the opposite of what we want, that is to to delegate this this logic to the collector.
But yeah, let me know what you think in the in the Pr. We can talk about it now. If someone has any ideas or we can talk about it over there as well.
and the second Pr is slightly slightly bigger. Change
that I made to allow us to to customize. Better how the collector merges, how the Supervisor merges all of the different configurations to
Nikolai, you! I'm not sure if you want to talk now or not.
**Andrzej Stencel** 44:14 You're muted, mikay.
**Mikołaj Świątek** 44:16 Alright sorry. But yeah, you can finish your thought. I wanted to ask about the configuration and reloading in general. But yeah, I can. I can do it?
**Douglas Camata** 44:29 Okay, the yeah. So the second Pr is is more about
customizing the the order in which the supervisor merges different configurations to build what we call the the effective configuration that the collector will be asked to load. I already got some review comments in the past. Everything is handled, I believe.
and it is good for for a second review
and also for new reviews. If if others are interested in this as well.
and yeah, I know that a bunch of people are going on on Pto, because it's
it's what happens in European summer. I might be going for some as well soon, so I know things. Take a bit longer than than usual at this time.
and go ahead, please, Mikolai.
**Mikołaj Świątek** 45:30 So when it comes to the
configuration reloads based on some signal. In this case it's it's the hangup signal. But there's been proposals in the past to make an Http endpoint. That does the same thing, you know, irrespective like you. Let's say you're the collector. You get a signal that tells you, reload configuration. All right. So you reload the configuration.
The configuration is invalid in some way, and what makes this more a bit more complicated or a lot more complicated, perhaps, is that you can find out if you find out your configuration is invalid.
syntactically in some way, as in you validate it you call validate on all the components, and one of the components tells you. You know I I don't know what this configuration key is invalid, then that's relatively straightforward. And in that case, May, it's it might be valid to just say, Okay, we don't reload this. We we keep our older configuration right?
But if you get a problem where, when actually starting the component, then you don't really have a way of backing out of that effectively like what you would have to do is start the whole component graph in parallel. But you usually can't do that because you might have resource contention between components. You have 2 Tlp receivers trying to bind to the same part.
You're good. It's it's gonna fail, anyway. So this is not. This is in general not such a simple problem.
And also I'm not sure if, like from from the perspective of the OP. Supervisor, do you not prefer, if the collector crashes in this case like, isn't it better that you immediately know
that something was wrong? Because normally like, if you, if if we do the 1st case where we, the configurations invalid. The collector knows, and and it just keeps the old one right.
How do you know like you would have to wait for status? I suppose? Right.
**Douglas Camata** 47:30 Yeah, yeah, we would have. We would have to.
Oh, yeah, that's that's we wouldn't get any status right, in fact.
Or is it.
**Mikołaj Świątek** 47:45 I mean you would get you would get status for the old configuration, depending on whether the like. The question is, how do you know whether this configuration was successfully applied in this case, like, Well, what kind of
facility do you have to to ensure this? So from this until that exists, and I'm not sure if it exists right now. I think not, and it's probably better for it to to terminate, because then, at least as the open supervisor, you know, and you can you? You can manually go and and roll back that configuration and start it again. And and then you know that this has happened, and you can report that back back up to your to your remote.
**Douglas Camata** 48:26 Yeah, yeah, probably that's that's better.
That's better. That's a better solution for now. Yeah. So just yeah, indeed, let it crash.
because at least we will know that it crashed
if it was working before, and we changed config, and it immediately crashed. Or it's not starting anymore. We know it's because of that.
and the collector can, or the supervisor can probably just revert what it is trying to do. And and then we let
we let that configuration be reported as as failed that that remote configuration.
But yeah, so it's it's a good problem to delegate
to to delegate. I mean to to postpone.
But we in the in the future, them there could be
slightly more elegant ways, let's say, of solving.
But yeah, it might. It might mix.
It's a, it's a complicated issue. Yeah, it's a complicated issue. If you have right. If you have just bad config that maybe you cannot even parse as ammo, or maybe values are out of range right? Maybe some integer that should be from that should be bigger than 0. Maybe someone put the minus one. There
can be can be very easily detected, and then you crash and.
**Mikołaj Świątek** 49:57 You know you.
**Douglas Camata** 49:58 Supervisor can handle it.
**Mikołaj Świątek** 50:00 You can. Because in the Supervisor you, you're starting the collector, you're you have to be able to start the collector
right? So you are able to actually call the collector binary.
and the collector binary has a has a validate command which you can actually run, and it will tell you whether the it will do the static verification. So that's something you can actually do before you even you even apply. If you get a new config, you can actually shell out to the, to the collector and and check whether it will accept. This will not save you from runtime problems which can still happen
that will save you from a lot of from like, probably from from the majority of of issues. This way.
**Douglas Camata** 50:46 Yeah, I think so. Yeah, that that's a good idea.
So we could do. We could call the collector
like validation, config validation function before doing any kind of
any kind of reload. In fact, not not only for the
for the hangup signal, but even when we use the
when we run the current, reload logic. That is, just stop and start the collector. In fact, we could just run the config validation before stopping
to potentially avoid downtime if if the configuration wouldn't start anyway.
**Mikołaj Świątek** 51:27 For for the record. I do think that send sending the sick hang up is is better than restarting the process.
but but yeah, I I think it should terminate if it. If if anything is wrong, that's just until there's a way to actually for to actually be able to report about this. Maybe you actually need like a
you. You might. We might. We might need things in the core framework that will let us do things like detect whether what configuration is active and and whether it's like the old one or the new one, and then the open extension could hook into that and do something. I I think that's like the
longer term solution to this.
**Douglas Camata** 52:13 Yeah. Yeah. And the and potentially, it is
this solution that you mentioned could be part of
it. It might also help some work on the collector to let it
to let it reload configuration without a supervisor process. Even.
Yeah. Might be there. There might be some shared logic. There.
**Mikołaj Świątek** 52:37 Yeah, you're it's probably probably it. It will eventually do that, although personally, with some experience from processes reloading and reporting their own configuration, I would rather not personally do that.
You can get into some funny states.
**Douglas Camata** 52:56 But that's a that's a that's a good definition. Yeah. But I, yeah, I think the behavior of the collector today it will be, it will crash. So I think we are good on that. And I might, I might work on this improvement as well on the on the supervisor side to use the collector binary to validate the config before attempting any kind of restart.
Thanks, thanks for the for the idea.
**Mikołaj Świątek** 53:39 I think we don't have anything. We don't have anything else on the list, right?
Are there any non-list topics we want to discuss
sounds like we're done. Then.
**Andrzej Stencel** 54:04 Thanks. Everyone.
**Roger Coll** 54:05 Thank you.
**Mikołaj Świątek** 54:06 Thanks everyone. See, you have a nice day. See? You.
