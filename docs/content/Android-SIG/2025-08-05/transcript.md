SIG: Android SIG
Date: 2025-08-05
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:49 Hello!
**Jason Plumb** 00:51 Good morning!
**Hanson Ho** 00:54 How's it going.
**Jason Plumb** 00:56 Pretty well. How about you?
**Hanson Ho** 00:59 My bad. It's cooled down the last couple of days to a manageable temperature. So that was good.
**Jason Plumb** 01:03 Hey? Same, it's been really nice. It's it's climbing back up a little bit today. But I haven't looked at the forecast. It's been. It's been good, hey, Jamie?
**Jamie Lynch** 01:11 Hey! How are you doing.
**Jason Plumb** 01:14 Pretty good. Where are you based out of.
**Jamie Lynch** 01:17 Manchester.
**Jason Plumb** 01:18 Oh, okay.
**Jamie Lynch** 01:19 Yeah. It's about 4 o'clock here.
**Jason Plumb** 01:22 Yeah, nice.
And you all are completely distributed. Right?
Like, yeah, no offices not really.
**Hanson Ho** 01:31 We had an la office. But then we realized, why, people weren't in there, and people that were were like 2 or 3 people. So it's like.
it's it's there as a repository for like stuff. So it's pretty expensive to to get a storage box. So.
**Jason Plumb** 01:48 Yep.
**Hanson Ho** 01:50 Yeah. Jamie's in Manchester. I'm Vancouver. The person on Android is in Argentina.
**Jason Plumb** 01:58 Cool.
Nice.
Okay? Well, very light attendee list so far. 2 min in and very light agenda. And by light I mean non-existent.
**Hanson Ho** 02:17 I feel I feel we're we're heading into the European vacation or holiday time. So like like Manuel, or or or
other folks based on their well, Cesar, I guess as well. We may see less of them this month.
**Jason Plumb** 02:42 Yeah.
definitely noticed that over here, too, with a bunch of my team being in Poland and Estonia and elsewhere. So
that's the thing. I was gonna just check on one of these recent Prs and see what the what the speed is like here cause it is vastly improved if I remember.
So this is just like a random, you know, dependency. Update, pull, request. 15 min.
**Hanson Ho** 03:07 Oh, that's 1 of the longer ones actually.
**Jason Plumb** 03:11 It's much better than it was. We go back.
**Hanson Ho** 03:16 No, the the settings made a a huge, huge deal.
**Jason Plumb** 03:23 Yeah, let's just go like back to June, like, here's here's 1, for example.
Oh, maybe I can't see it anymore.
**Hanson Ho** 03:33 It it it was significantly I I didn't go back to June. I went back to the couple of weeks that that before all the changes, and was like 40 to 50% faster.
**Jason Plumb** 03:44 Alright! So this 1, 23 min! Look at that.
**Jamie Lynch** 03:49 Nice.
**Jason Plumb** 03:50 That's the 8 min improvement that's huge
shaved off like 30%. Almost. That's awesome. Cool.
**Hanson Ho** 03:58 Is, is the Ksp stuff done, or is that ongoing Jamie.
**Jamie Lynch** 04:03 Yeah, I'm still gonna take a swing at that. So yeah, basically, I think migrating from capped to Ksp, should make stuff a bit faster just in general, which could help with build speed, I guess. But there's a few things that I'd need to do to a project to get that?
yeah, I think
there's an auto service annotation which basically adds, like meta in files. And that isn't compatible with Ksp.
**Jason Plumb** 04:34 Oh!
**Jamie Lynch** 04:34 So I think the solution I was planning on using was, I think
there's a Kotlin equivalent of also service.
So I was gonna switch out that dependency. And
I think anything annotative or auto service would probably also need to be.
**Jason Plumb** 04:56 Yeah, we use it for all of the instrumentation. Yeah.
**Jamie Lynch** 05:00 Yeah. And I mean, an alternative is we could figure out some different solution for those meta info files.
**Jason Plumb** 05:09 Yeah, I mean, we're using it for the service locator stuff. Right? So there's code. That's like, Hey, I want to find all the instrumentations that are on the class path, and it just looks for that annotation.
If there's a more colony or a more android way of doing that sort of thing absolutely seems welcome.
**Hanson Ho** 05:27 As long as we don't need to do that and use like generic Java instrumentation. Expect that to work
**Jason Plumb** 05:35 Yeah, I mean, what do you? What do you mean by generic cause? They definitely use auto service over and instrumentation.
**Hanson Ho** 05:43 Yeah. Well, so so if everything inside the project we can control and kind of redo via via, you know, cotton friendly annotations and things like that. We're still gonna bring in, or other people potentially can bring in other instrumentation that do use auto service and making sure that that would be compatible with what we do.
**Jason Plumb** 06:01 I see what you're saying. Yeah, cause I mean, this technically is an Api change. Right? If we if we change this from, if our contract is like, Hey, don't use auto service anymore. Use some other mechanism. Then that's a that's a breaking Api change.
And because we're not stable, I don't feel super bad about doing that. I don't know of any
3rd party or custom
instrumentations that anyone has written. So maybe you know I hate to. I hate to tiptoe around a breaking eye, change in an unstable release for something that people may not yet be using.
But also, you know, we we open telemetry need to be a little bit careful about
thrashing too much and imposing that kind of pain for people.
My my suspicion, my gut, is that right now changing auto service to some some other mechanism would not be too painful. But I would love to hear from other other
other voices.
**Jamie Lynch** 06:55 Yeah, just a note on
the solution I was planning on using. It would still use the same annotation. So it's still depending on like, I said. But I think it depends on the Google Annotation. But then
the actual, like annotation processing side of it is different.
**Hanson Ho** 07:14 That'd be cool.
**Jason Plumb** 07:16 That's where we have the instrumentation loader, or whatever it's called. I forget it might be in the
SDK pre-configured run builder.
**Hanson Ho** 07:28 So. So you say you're changing up the annotation processing. Perhaps the Kotlin annotation processing.
**Jamie Lynch** 07:36 Yeah. So basically, it'd be the same annotation. So the Api shouldn't change in map respect, although it would need to be a Kotlin class. If we basically
go with that.
But yeah, be.
yeah, the actual annotation process would just be not Google's 1. It would be I think Zach squares has developed one.
**Hanson Ho** 08:03 Yeah. And it should just be a a project change on our side. Take out the the plugin that does current the process of the current annotations and then stick in this other one.
**Jason Plumb** 08:11 So it would not be the service loader anymore. It would be some other mechanism.
Is that what I'm hearing.
**Hanson Ho** 08:20 No, I think it's the in the processing side right, Jamie.
**Jamie Lynch** 08:23 This code, this code, this code stays the same.
This should all stay the same.
**Jason Plumb** 08:29 So that sorry? I don't think we have an explicit annotation processor for for auto service, do we?
I don't think so.
I think it's just a normal part of like Java compilation, which I know, you know, Android Android special that way.
and I think the auto service annotation is retained meaning it. It propagates into the class definition.
I'm just. I'm speaking more on the Java side of things.
and because it's part of the class file definition. You can find all classes that have that annotation which is what the service loader is doing. It's saying, Give me everything that has this.
So where is it different, or what am I missing.
**Hanson Ho** 09:15 I thought it was the Meta in classes that get generated by by the builder, or some part of the process
right.
**Jamie Lynch** 09:23 Yeah, I think my understanding is not like
particularly great around this, but I think the annotation should still be retained in the byte code.
So it'd be fine to quite up like this.
And any class with that annotation.
And then a compile time. Basically, there's just a
plugin for the build, but is looking for auto service, and then it creates Meta and files.
**Jason Plumb** 09:57 Cool. So there's a there's a compilation or build time step rather, that's finding all those auto services and and putting the class names into these service definition files, these meta and files, or whatever.
**Jamie Lynch** 10:09 Yeah, yeah, I think so.
**Jason Plumb** 10:10 Okay. So that mechanism is what would need to change. To support is a Ksp.
**Jamie Lynch** 10:15 Yep.
**Jason Plumb** 10:15 Cool.
Okay, that sounds great.
I've been awake for minutes, so bear with me.
**Hanson Ho** 10:40 so I think, right now, I mean, there's 2 reasons for that, change, I think, one is
think that this would be that would be the biggest block or at least it was before all the settings changes. I think it was like running at 3 and a half minutes, or something like that. And also
capped is in is is not deprecated, but maintenance mode so you know, it's liable to break hit some feature point. So it's always good to to kind of move off of that.
And if we don't have to change Apis and that use different annotations and stuff like that. That seems like it's it's worth worth while looking into.
**Jason Plumb** 11:16 Agreed.
Okay.
yeah. Those who joined most recently feel free to add anything to the agenda. It's very light, and we have a light attendance today as well. So
feel free to add whatever you'd like in there.
or just to just to unmute and say, Hi! And what do you want to talk about?
This came up. This came up in slack for those who didn't see it.
There was an ask from this person around finding documentation for our what I would describe as like pretty darn complicated delegating exporter chain. So we have an exporter and the exporter
buffers telemetry early in the life cycle, because the SDK. Is not prepared yet, and then, once that but once the SDK is ready that buffered that in memory. Buffered telemetry is then delegated to another exporter, that exporter, then delegates to one of several different disk writing disk, buffering exporters, and there's another process that comes and reads those that whole. The way that that is all plumb together is like fairly complicated. And so it's a completely reasonable ask, I think, from this person.
To have documentation around that. And so, yeah, I was like, please open an issue. I think this would be a good thing for us to have
we, like most of the other projects, have some amount of documentation in the repo, and we just don't even have a docs
like Directory. Yeah, there's like no documentation in here. And you can imagine someone coming to this like for the 1st time and wanting to know how to use this. It's like, it's pretty darn light. So I know there's some other documentation. I think I tagged it. Yeah, I think there's some other documentation stories. But
this one's getting close.
But yeah, just any like overall documentation is like pretty lacking in this project. And I think that having that built up a little bit could probably also help adoption or interest from people who just stumble in.
Yeah, this one's getting close.
So help always wanted with that.
while we have a light agenda. I want to remind everyone who's on the call that we can always use help with reviews.
And if you're looking to expand your influence on this project. The number one way you can do that is, by reviewing pull requests
and providing comments on those pull requests. So if you see something come in even if it's just these. You know, we have a lot of these renovate Prs.
but even something like that is helpful. But like, for example, I haven't seen this yet. You can tell by this blue line. So I come in here as a Maintainer, and I'm like, what is this all about? There's already 5 comments. It's not. It's non-trivial. But if other reviewers have come in and commented, now now, I have a lot of context here. And I can. I can get caught up to speed really quickly on this. So
reviews always help.
and we do require at least one review before merging anything. So if someone adds a Pr, we need it to be reviewed, because, especially if that person is me, I can't review my own Pr.
If that person Cesar, same situation, so please help.
**Hanson Ho** 14:34 And only Jason and and Cesar can merge. So you know.
**Jason Plumb** 14:38 That's true.
**Hanson Ho** 14:38 There's always a gate, so don't worry about about oh, no! If I if I if I review this and you know what if what if you know so don't worry. One of them will be will be on the hook for merging. So.
**Jason Plumb** 14:50 True. Yeah, absolutely. And we have good time zone coverage. There. Right? We have. We have Europe, and we have West Coast us. So it's we have pretty good
balance there as well.
but always looking for P. Always looking for help, and people that want to expand their influence in the project.
Okay.
Alright. Somebody wrote Colin Api Update.
**Hanson Ho** 15:26 I did. Jamie, do you? Wanna do you wanna just get a quick update about the progress there? Or do you want me to.
**Jason Plumb** 15:33 This is the thing that embraces building.
**Hanson Ho** 15:35 Yes, that eventually will be donated. Fingers crossed.
**Jason Plumb** 15:39 Cool.
**Jamie Lynch** 15:43 Hanson, do you want to take it? Maybe.
**Hanson Ho** 15:45 Sure so a couple of weeks ago we so for those of quick, add links. Who may not know embrace is working on a call, and Api and the company SDK, so that we can have a mobile 1st call
Kotlin SDK implementation that we could use in multi-platform projects which, with Java, we can't do right. Now. 1st thing we're going to do is the Api, and then with the set of adapters, so that you can basically use the Kotlin Api and the Java SDK and all the ecosystem stuff
under the hood right now, embrace is in production with that architecture. So we use the core. Java SDK, the Java SDK,
but then our internal code calls it through a cotton Api and the adapters. We did a bunch of proof testing on it. The extra
extra overhead, it adds, is trivial, and we are gonna kind of keep adding to it and prove it out until we get to an Api that we're happy with and then we're gonna
create an official project and try to get folks to to come on board and get it donated. Of course we need a whole bunch of things to do that. We realize that. But you know the 1st step is is actually eating our own dog food. And this is what we're doing. Things are moving fairly quickly. And I'm really happy to see the progress. But until this actually gets into
hotel fans or Cncf, you know the
it's still kind of very, very not done so hopefully. This will happen soon, but we don't want folks we don't want to donate to hotel without thoroughly, you know, vetting on ourselves, so we're in that process.
**Jason Plumb** 17:38 Superior org, and Github.
**Hanson Ho** 17:40 In embrace. Dash I/O slash and telemetry Kotlin.
**Jason Plumb** 17:47 I just wanted to link to it. Great.
**Hanson Ho** 17:56 Thanks.
**Jason Plumb** 17:59 And are you using from the SDK that you're wrapping the Java SDK, are you using any internal classes.
The top of your head, because I think we might be in Android.
**Hanson Ho** 18:13 You mean SDK span, and things like that.
**Jason Plumb** 18:15 Yeah, but anything that's in an internal package. This is this is not gonna find what we want. But.
**Hanson Ho** 18:23 I.
**Jamie Lynch** 18:24 Like a few things like getting the span context key.
But the majority is just using public Api.
**Hanson Ho** 18:34 Yeah, there, there's there's there's a there's a I mean, we're gonna do document this. And and you know, write out more when we actually are able to. But there's a there's a bunch of stuff that's
the SDK and SDK and Api divide isn't super, you know, separate, or ought to be and there's like bunch of internal, static, final declarations of keys and stuff which is effectively just a string or just a you know it just happens to to live in that package. So we we the wrappers.
so obviously the SDK. Eventually, when we actually have it, we'll you know we'll have a Java references. And I think our we've we've tried to minimize the the use of in the adapters. Internal.
**Jason Plumb** 19:20 Sure I mean
always a good idea. You should never use internals from another from another package. But like so here's 1 example of where we do that. I I don't remember the reason.
**Hanson Ho** 19:33 For it.
**Jason Plumb** 19:33 But in in this Okhtp instrumentation we do reference this internal class, which is the default builder, and I think there are a few other places like maybe
like this is, this is in
an instrumentation package which might also like.
get us access to some stuff
like we might be shadowing this package. But whatever outside of in outside of instrumentation, I'm worried, or I'm interested in knowing, like what
what we're importing out from outside of Android, that is internal.
and I thought the logging stuff was also one.
**Hanson Ho** 20:16 Well, I I wanna say, if, like any references to that would be in the adapter modules.
**Jason Plumb** 20:24 Yeah, that's smart to kind of keep it isolated.
**Hanson Ho** 20:27 Yeah, the adopter modules most, we we've been able to find ways to kind of work around a lot of the the
issues where things are only exposed in certain interfaces in the SDK but for the most part everything's been okay the one exception that we found yesterday. Was setting the
updating the span name in the processor on start because we we expose a bit more on the on the column interface for span. Specifically. You know things that you could. You could read the state of of span which you know, in the in the Hotel Api. You just can't do that.
**Jason Plumb** 21:10 Right.
**Hanson Ho** 21:10 So.
So there are a few things that we had to like, you know, do a bit of things. But
obviously things will be documented when it's out in terms of like compatibility issues. Working around the context stuff is is a bit interesting. Just because
well, you can't rely on on current, on Mobile when you, your instrumentation doesn't control the execution of the thread, relying on current is extremely dangerous. So setting using scope, and you know. But you know again we're hoping to prove it out, and we've been using the android, the android as a as a testing bed for for doing migrations and porting, and things like that.
So
**Jason Plumb** 21:52 Cool. Nice.
Yeah. The thing I think I was conflating was incubator with internal like, it's this.
And this is just like stuff that we know is going to be changing when it finally lands. So maybe maybe our usages are not that bad
of internal classes which is great, which is what you'd want to see.
**Hanson Ho** 22:11 I would hope there'd be some
package protection, or like private, like, you know, access protection for internal classes
**Jason Plumb** 22:20 Yeah, but you can't always do that, because I mean, especially in Java. You might need to
reference it from another package, which is in the same module. It's not necessarily one package per module
cool. What else do people want to chat about?
**Hanson Ho** 22:40 Oh!
**Jason Plumb** 22:44 We don't have to use the full hour, but we can also just go over like new issues and new pull requests. So there's a bunch of dependency stuff, and it says our. I think.
said that he had one, didn't he?
**Hanson Ho** 22:56 Are there any
**Jason Plumb** 22:58 Understand.
**Hanson Ho** 22:59 Are there any outstanding things that we talked about the last couple of times that anybody wanna excuse me.
**Jason Plumb** 23:08 Let's go review it.
**Hanson Ho** 23:12 Cause. I remember there was a couple of things that came up last week and the week before about
forgot now what it was.
**Jason Plumb** 23:21 So Mustafa brought this one up. Origin, this.
**Hanson Ho** 23:24 Oh yes!
**Jason Plumb** 23:25 Up originally. I think there was this user who was trying to close the Android SDK and create a new one. And I created a Pr that I think I merged.
Well, let's see, we'll shut down. Yeah. So I I added this a few days ago.
and it's a start to like shutting stuff down. So there is now a shutdown method on opentelemetry. ROM,
And it's only tested in so far as I think I I think I might have called it from the demo app, and then I didn't try and reinstantiate stuff. I'm just like it didn't crash
like. So it's it's it's pretty experimental. But it is on the interface
and the implementation. If you haven't read this yet, go take a look. It's like I I think it's fairly interesting, because there's a lot as we expect. There's a lot of moving pieces, and to shut them all down cleanly. This is just a start to that. We have this whole subsystem called services, and that's supposed to be like this facade in front of like android platform type services. And those are not being shut down yet. I think Cesar wanted to. He offered to like.
maybe take that on
But
is there another? Yeah. So there's also a shutdown or sorry. There's an uninstall just to have parity between the install method on instrumentation. Now, there's an uninstall.
and there's a default, no OP implementation. But if if instrumentations want to override that, like slow rendering does
when you call uninstall
it checks to see if it's already been shut down in the dumbest way possible, and then it unregisters listeners. Right? So this is like pulling stuff back out of that have been registered previously.
and then delegating to more shutdown. So you know, this is this is like a start.
More eyes on that always welcome.
and there's more to do, I'm sure. So if you if if when you're in the code, you see this and you're like, Hey, I wonder how that shuts down? Just something to keep in the back of your head. I think.
**Hanson Ho** 25:32 Now the services stuff is gonna be a bit tricky. If there's instrumentation.
not in this project. That depends on it. It's like, you know, what is this intermediate state when it's shutting down? And
are there? Are there expectations not met, and things like that? But it's really gonna be hard until
you have instrumentation that does things in that weird way. So it's almost like we set out the expectation that you know there could be a state where these are things are not available, and whatever we publish shouldn't depend on something that
you know we expect could change state or be null or whatever
So we should probably test our interfaces. When we, when we actually do that for the services.
**Jason Plumb** 26:13 Yeah, and having, like an integration test that sh that like creates, creates the open telemetry. ROM. Instance, does something, gets telemetry, shuts it down
and then creates a new one like that would be a great integration test. We don't have that yet.
Jason. I totally missed that. Pr. I didn't see it go by.
It was only for a couple of days, so please take a look.
**Mustafa Haddara** 26:39 Okay, I'll take a look. What?
So you just did this for the slow rendering instrumentation. Did you.
**Jason Plumb** 26:47 It looks like that was the only instrumentation that I touched. I can't.
**Mustafa Haddara** 26:51 Okay.
**Jason Plumb** 26:52 And I think it was intended to sort of show the pattern I did. We absolutely need to go through all of the other instrumentations, and and see which ones, you know, warrant a shutdown.
**Mustafa Haddara** 27:02 Need. Explicit. Yeah, okay, cool.
**Jason Plumb** 27:04 There are definitely others.
that register listeners and stuff on install. They need to to have similar prs. This just kind of sets the the framework up for it, and then the one instrumentation.
So yeah, any other. Follow up Prs that want to attack the rest of the instrumentations would be super welcome.
**Mustafa Haddara** 27:26 Yeah, okay, cool. I can take a look at some of that. I was.
I think I had a to do list item from whenever we talked about this, to start looking at this, and
Glad you got there first.st
**Jason Plumb** 27:40 Cool. Yeah, I said, I would create a tracking issue, and I think I haven't done that. So let me add an action item for myself.
**Mustafa Haddara** 27:46 Okay.
**Hanson Ho** 27:52 So they're still needing to test the restart works. And and I believe,
multiple instances we said we weren't gonna support that.
**Jason Plumb** 28:05 Multiple, simultaneous, concurrent instances is not something we're super excited about.
**Hanson Ho** 28:11 Okay.
**Jason Plumb** 28:13 Yes, and I don't know. I've I've I had Friday off, and I haven't been paying enough attention. But there was
There's an issue that someone filed about this.
Where was it?
Was it? It was based on this one. I think it's this one.
So where do we leave this one off. I think, Cessor chimed in. Okay, so yeah, if you haven't read this one.
there's a lot.
**Hanson Ho** 28:41 Right.
**Jason Plumb** 28:41 There's a lot of words in this.
but this is the person that instigated having multiple instances.
So it's 1 1. 0, 3. And
yeah, we can't read this on the call because it's too long. But I, I responded, based on our conversation from last. Sig, we're like, you know it seems like shutdown and restart is like reasonable.
multiple, concurrent. Seems like a recipe for disaster, if not
pretty high overhead, like. I don't know why you would do that.
Their their model seems to be upside down a little bit. Right they were, I think, coming from this library perspective, where they wanted like a library to be able to report its own usage metrics. But they're all they also wanted to leverage a bunch of different parts of the open telemetry room
seemed maybe
weird or misplaced. But I would think that really the project was designed originally to like do application level user monitoring
and not, you know library monitoring, which may be a different beast. I don't know.
**Hanson Ho** 29:45 Well, I think we came to the conclusion of you. Should they should be able to start a multiple instances of the job. SDK, and basically use that but the the application hooks and things like that is one to one with the application itself. So it doesn't make sense to have, you know, multiple registrations of of
of you know, lifecycle handlers to report. You know that that doesn't make sense. So did they say anything about, hey? We can't use just the Java SDK we need, you know, some platform shims, or whatever.
**Jason Plumb** 30:22 They did, yeah.
**Hanson Ho** 30:23 Okay, is that why? Okay.
**Jason Plumb** 30:25 Yeah, there's like some. There's some other components, and I think it goes beyond just the disk buffering. But this buffering was one like disk buffering and contrive. You can wire that up to the SDK. You don't need. You can do it the same way that that open telemetry roam, does it.
But I think there were some other things, too. They wanted to leverage, and I forget what they were. But they're mentioned in.
**Mustafa Haddara** 30:45 And we don't.
We don't have this buffering on by default, right.
**Jason Plumb** 30:51 No, there's an issue for that. We want it to be enabled by default. So please, if anyone wants to make that change.
there is an issue to do it by default. This one.
**Hanson Ho** 31:06 I think I think it's it's it's more more of a Api behavior change. That was the worry and not the actual code to do that. I think.
**Jason Plumb** 31:15 To do this.
**Hanson Ho** 31:17 Yeah, I think it's just a flip of the switch right.
**Jason Plumb** 31:20 Just a matter of wiring up in the agent. Initializer, I think, is.
**Hanson Ho** 31:25 Clock.
**Jason Plumb** 31:26 Yeah, and it's not there, currently.
But yeah, I think there's just a I think there's some conf there. I think there's a disk buffering config, and if you enable it via that, I think that's all you have to do.
**Hanson Ho** 31:39 Yeah.
**Mustafa Haddara** 31:40 I can leave this comment on the on the issue. But I think
when I was looking at our disk buffering, it's still like labeled like heavily experimental or whatever, and we'd wanna not label it experimental if you're gonna turn it on by default.
**Jason Plumb** 31:59 Because it discourages people from using it.
**Mustafa Haddara** 32:03 I mean, I think if it like, if if you're labeling something as experimental to me, it it reads as like.
Oh, this could blow up in your face, and
**Jason Plumb** 32:16 Yeah. So there, I think, in the spec or in the community repo, I forget which. There was some discussion of this, and the
I think the takeaway was that they have decided to stop using the word experimental, and they've renamed it to development.
which just means it's like under active development and not not yet stable.
And I think I think that's just a like a.
it's, it's a phrasing change just to like. Because, yeah, I agree that when people see the word experimental they get, they get pretty twitchy, and they're like, why would I use that as experimental?
But.
**Hanson Ho** 32:56 Feel like we could probably
either take that word out like, I mean, I I think the sentiment of it being unstable is is what we're trying to to convey, and people are rubbing up against. I think this
is beyond that now, right like it's been out for a while folks have been using it. It's probably not issue free. But we know that without this buffering you lose a ton of data. So it's almost like you're you're you're you're by default, losing data when when your network is unstable or when you're offline, or when there's a crash. So you know
the worst is always gonna happen without this buffering, and this buffering enables or or at least makes
the the more basic of those cases work better. So unless we're we're thinking that this causes crashes or drops telemetry needlessly. This is just going to be better. So maybe we should take a look at making it not experimental, just saying, This is, this is
pretty good.
**Jason Plumb** 34:06 In contrib. It's labeled currently as Alpha. I think there's a probably I agree with what you're saying, Hanson. There's probably an opportunity to move it to Beta Mustafa. Do you specifically see the word experimental for this feature anywhere?
We can just look for it in here, too.
**Mustafa Haddara** 34:28 Yeah, I remember. I don't see it anymore.
I do see a a in the android repo. There's a features disk buffering Directory.
Where we configure it all, and I thought there was a read me in there that said Experimental.
Oh, okay, there isn't.
**Hanson Ho** 34:51 Very likely that was added initially, and just never touched.
If it's a rebate.
**Jason Plumb** 34:58 Yeah, this features thing. Oh, man.
**Mustafa Haddara** 35:03 Yeah, there isn't anything in there. I might be.
**Jason Plumb** 35:06 It's the only.
**Mustafa Haddara** 35:06 Might be thinking.
**Hanson Ho** 35:09 It could be a cold comment, you know, as far as so.
**Jason Plumb** 35:12 Yeah, I was curious, but we should. We should find this stuff, and at least change it to under development.
or, you know not the word experimental. Those are also valid changes
like here. This one's weird, you know.
I think that I think that might come from upstream. I forget.
**Hanson Ho** 35:32 It's c, 3, 3, yeah.
**Jason Plumb** 35:39 Well, if it comes back around, you know, let me know. There's just it looks like only 7 matches here in code.
and they're mostly around this Http stuff and the volley client.
Okay, so what do you like? Do we think it's important to maybe work on moving wherever it went toward Beta.
**Hanson Ho** 36:03 Yeah, I think we should create an issue for it, if nothing else.
**Jason Plumb** 36:10 Are you offering to create an issue for it, Hampson?
Sure it's in Java. Contribute.
**Hanson Ho** 36:18 So.
**Jason Plumb** 36:32 And I don't. There, I don't know what the criteria for that is, and like what it takes to go from Alpha to Beta and Beta to stable. Do we like we have one stable component here.
but it might just be a declaration from the component owners. I forget.
**Hanson Ho** 36:51 Can we just change? Just put a Pr to change that?
Read me.
**Jason Plumb** 36:56 Yeah, cause I'm not sure it's anywhere else, although it might actually be
in the version. Let's see if like, let's just pick one of these
and look at the build gradle.
Does it have the word Beta in here?
What am I doing?
Oh, it's getting worse. Okay, no, Beta.
So if we go to Maven, we look at Contrib.
Gcp. Is this the latest pretty new still? Is Alpha
all right? So this is also something to raise
with Contrib, for which I am a maintainer.
**Mustafa Haddara** 37:49 Yeah. The fact that these publish with Alpha. I don't know what we I don't know what we're gonna do about this, but we should change that because it it doesn't.
**Jason Plumb** 37:56 Reflect what's on the main page of the readme.
Alright, I will take that as an action item to file an issue on. That.
Is that true of the stable one as well. So aws resources.
Alpha, right? In the name. Okay, that's a problem. I'll take that one on.
Oh, fun.
Yeah, did this land? Did did this come back around? Do we remember? I don't remember.
**Hanson Ho** 38:54 Oh, I I thought I thought we decided to remove it and just say, people included in the in there.
**Jason Plumb** 39:00 Right. But did it? Did a Pr. Or an issue land for that.
**Hanson Ho** 39:04 I haven't seen it.
**Jason Plumb** 39:05 Okay, I haven't seen it, either.
0 closed. Okay, I don't know.
Oh, Pr is welcome. There is another like issue about phone state. So I'm not. Gonna we don't need to create one. There's 1 that
it's like a year old. It's like we should probably remove breed phone state.
**Hanson Ho** 39:29 Yeah.
**Jason Plumb** 39:36 Yeah, this is some of the flush stuff. Okay.
does anyone have anything else they would like to talk about?
**Hanson Ho** 39:48 There's the client meeting in at 9 as well, so we have it this week.
**Jason Plumb** 39:53 It's true.
**Hanson Ho** 39:53 Gross.
**Jason Plumb** 39:55 Yeah, half an hour. So the things that are on my brain on the client stuff is
the jank, pr, that's still out there.
if you all haven't, I mean, that's
I I have like finally have, like 2 things I need to respond to.
Cool.
**Hanson Ho** 40:20 Yeah. Github.
**Jason Plumb** 40:21 Very github.
Oh, whoops.
huh!
And it fooled me.
Hmm!
**Mustafa Haddara** 40:40 Yeah, I was trying to dig up a Pr of mine and hit the same thing, I think. Github's having some.
**Jason Plumb** 40:45 Yeah, they just haven't caught it yet. Must have just happened, anyway. That jankpr. The last I remember is Lou Miller, who's the Maintainer, gives gave a couple of comments. I just need to respond to those. But I think it's getting pretty close. You can see that there was a
Well, even, that's
okay. Yeah. So there were, you know, a lot of comments on this already. So we've done a lot of work there. I think it's getting close, and then I think
someone else had. Well, I won't be able, probably won't be able to find it out. But someone else had.
I think there was another semantic conventions. Pr. That was Mobile, related.
**Hanson Ho** 41:24 Yeah, the the Joe Joe to Thompson guy, I think, had it so.
**Jason Plumb** 41:29 Oh, yeah, yeah, that's right. Was that gonna? Land? Was it? Good? I forget.
**Hanson Ho** 41:33 I was, yeah, I need to take a look at it. There was a bunch of stuff on there.
**Jason Plumb** 41:41 So no, that says ours, okay? So maybe this, oh, okay, I'm gonna stop clicking on github now.
**Hanson Ho** 41:46 They? They were talking about the app app name versus service name. And and I was gonna point into immediate discussions that have been had we realize.
**Jason Plumb** 41:57 I did that.
**Hanson Ho** 41:58 Oh, okay. Perfect.
**Jason Plumb** 41:59 Yeah, so where is that one? Let's see.
**Hanson Ho** 42:01 Button. You can't click on.
**Jason Plumb** 42:04 I know.
Well, maybe, is it this one? No.
there's a bunch of stuff in here.
**Hanson Ho** 42:16 I have it in my emails, probably.
**Jason Plumb** 42:20 Oh, you have emails, notifications turned on. Huh?
**Hanson Ho** 42:24 Just for open telemetry, Andrew, because that that's the one I miss the most. So I I not that I read all those emails, I should say, but you know I might have to go find it.
**Jason Plumb** 42:35 Yeah, your portion.
Oh, my gosh.
**Hanson Ho** 42:40 Yeah, well, that's why I don't really use it. I guess I do it to myself.
**Jason Plumb** 42:44 I think I'm sitting north of 400 right now. Let's see
4, 15. I'm so far behind.
Yeah, I I don't have emails turned on for this, it would be overwhelming. And I would miss important emails.
**Hanson Ho** 42:56 It's it's 2, 4, 3, 0 last updated August first.st If if that means anything.
**Jason Plumb** 43:02 It does.
2, 4, 3, 0. I love this.
It's backup plan.
So that's why I didn't find it, because it's on the next page. Probably.
**Hanson Ho** 43:14 Oh, it works again.
**Jason Plumb** 43:16 Does it?
**Hanson Ho** 43:17 Oh, you you click next right.
**Jason Plumb** 43:19 Yeah, 2, 4. Let's maybe there it is.
this one. It's gonna work. Come on.
Oh, we tried.
Aha! There we go.
Well.
**Hanson Ho** 43:46 I'll go through that my backlog of of things to comment on and and take a look. Yeah.
**Jason Plumb** 43:53 Okay? Well, hopefully, this won't be an all day thing. Hopefully, it'll be like a little bit of time thing.
**Hanson Ho** 43:59 Okay.
**Jason Plumb** 44:01 The white space. The empty space surrounding
on this call seems to be lighter than it normally has been. That's weird.
I suppose Zoom is freaky, anyway, that's unimportant.
**Hanson Ho** 44:14 Okay.
**Jason Plumb** 44:14 Thank you for joining folks. Clever chuck, you join late. Do you have anything for us before we call it a day?
**cleverchuk** 44:22 No.
**Jason Plumb** 44:23 All right.
Well, cool, appreciate you, and thanks for the reviews, and we'll see you in the comments.
if not on the client meeting.
**cleverchuk** 44:32 Damn!
