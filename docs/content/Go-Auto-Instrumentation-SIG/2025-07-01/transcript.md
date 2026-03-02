SIG: Go Auto-Instrumentation SIG
Date: 2025-07-01
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:53 Hey Mike.
**Mike Dame** 00:58 Hey? How's it going.
**Tyler Yahn** 01:00 Going pretty good. How about you?
**Mike Dame** 01:02 Good.
**Tyler Yahn** 01:05 Any plans for the holiday weekend.
**Mike Dame** 01:08 Oh,
yeah, not too much. This weekend. We're gonna be traveling next week trying to do some more work for this house. We're we're building in New York. So
got some stuff next week. But yeah, just kinda hanging out this weekend and enjoy some time off
moving to New York. Isn't that like the arch sin of a New Englander?
Well, I'm originally from the area.
**Tyler Yahn** 01:33 Oh, really. Yeah.
**Mike Dame** 01:35 Yeah. So yeah, I've been for about 10 years. So it was kind of an arch sin to move here.
**Tyler Yahn** 01:42 Yeah, don't tell me you're a Yankees fan next, right.
**Mike Dame** 01:47 No, yeah, I didn't really start watching baseball till we came out here. So it's now I get to be that that guy living in New York, the red Sox fan.
**Tyler Yahn** 01:55 Right? Yeah, yeah, that was always such a passionate argument. When I was out there, I just
I thought it was funny more than anything.
**Mike Dame** 02:05 Yeah, and you get to. There's like a weird mix. You know, some areas that are really 50 like, split like swing state like Connecticut. It has, you know you're either Yankees or Red Sox. There.
**Tyler Yahn** 02:16 Yeah, right? Yeah, it's such a such a funny one. But then the patriots is way more universal, I think, across.
**Mike Dame** 02:22 Yeah, I think anyone you know east of New York is.
**Tyler Yahn** 02:28 But I think it's just because the giants are really bad.
**Mike Dame** 02:31 Yeah.
**Tyler Yahn** 02:32 So, as far as I know, I don't follow too closely. But yeah, hey, Ron.
**Ron Federman** 02:39 Hey? What's up?
**Tyler Yahn** 02:41 Not much. Do you have a good vacation?
**Ron Federman** 02:43 Yeah, really enjoyed it.
**Tyler Yahn** 02:45 Nice. Yeah, taking the time off
speaking of vacation. So it's Canada day up north and
So I don't think we're gonna see Raphael or Nicola based on
what they added in last week. I think Raphael was talking about that, so we could probably get started here. I don't have too much to talk about. Actually
3
but yeah, get our names to the agenda. And then if you guys have things you wanted to discuss. We can
talk about them. I wanted to start us off by just mentioning this milestone we had talked about it last week. Ron, you were out. But there's only one other thing on here which is also one of the Prs I wanted to talk about today.
And this is this distro version. So I had said that like I,
I saw your comments. You're pretty sure you're up on this discussion. But just maybe, for people who are watching the recording. The idea is that like this is adding the distro version to our
default, pipeline
which is important, because otherwise it doesn't actually like identify the SDK, that's being used.
So it's definitely a positive change. There's a problem with like module, cyclical dependencies. If you try to do this in the wrong way, and
the other hard place this is in between is that this doesn't actually
work with the tooling to do our releasing. So right now, this version won't get updated when we do a release. So we have to go in and we'd have to manually address this.
So this is something I was looking to try to like Fix. I couldn't actually
figure out a way to do this without adding another module into our internal packages, which actually
is a really bad idea, because then you have these cross module in internal dependencies. So someone could upgrade the internal dependency and and just completely change the version number, but also break things if this Api ever changed. So that's usually not a good idea. We've moved pretty hard away from this in other packages trying to do that.
So the other option is, we can just have the release tooling. Update this. And so I'm looking at doing that right now. I'm working on a
got an issue tracking this upstream in the file. I started looking at it yesterday.
and it doesn't look. Doesn't look like
it doesn't look that hard. It also just looks kind of hard. It says that like it doesn't look very hard because it's just adding fields to a version file. It is annoying, because that project upstream is a little bit abandoned in some not necessarily abandoned, but just. It's not really well maintained. So the code is a little spaghetti code right now. So trying to wrangle a little bit of that, but hoping to have a Pr to address this up today, actually.
And then there's a really fast turnaround for the multi project given. We're the only consumers of it. So, yeah, that was the idea.
I did want to block this on
on merging prior to getting some sort of other alternate solution in or release tooling. Just because this is the kind of thing that like.
we want to make sure we get right.
So yeah, I was kind of wondering about that one. Ron, does that make sense.
**Ron Federman** 06:29 And yeah, I have 2 small questions, and the 1st one is you said that this is not used by like the hotel. Go. Repo doesn't use this multimod tool.
**Tyler Yahn** 06:43 No, they do so go does the trip does. The collector does? It's all it's all internal use. Yeah.
**Ron Federman** 06:53 And and currently, like
the code, there assumes that it's like this version, dot, go, file is in the root Directory.
**Tyler Yahn** 07:03 Yeah, exactly which we can't do. Because then you have a
module package cycle. Right? Is kind of the problem.
**Ron Federman** 07:14 Yeah, but.
**Tyler Yahn** 07:14 But yeah, normally, it's just it's, I think. Actually, we already have this right? Yeah. So it's similar to here, like, we have a version echo. And
it's not only the Root Directory, it's the Root Directory of the module. So like this is important for things like Contrib, where especially here, you have modules that are very like
random, not random, but like
very different version, information can be associated with one module versus another. So like this one also, like you can see like a version, dot go would exist here.
So yeah, this is, this is how this would look.
So all the the root path for the module is where the version go is is located normally.
And it's yeah. I mean, I can. I can walk you through what I'm thinking here.
Actually, that might be helpful, since we have a light agenda. And this is.
and maybe just a sanity check. So the multimod tool is here. It's a cobra command is how this is structured.
You can go through it essentially like there's a run command here, but all the internals are actually in here it's structured. Such there are multiple like sub commands. Each one of these is a sub command. Except for the shared, which is a shared module.
Pre-release is the thing that we're looking for. Pre-release is the thing that actually does the update of all the versions, as well as syncing all of those versions to the other module files and then updating this versiongo file.
Inside this pre-release. Here there is a update. All versions, all version go
like I said, it's not the cleanest. But then what this is essentially looks at all the module paths, and for each module path it looks to that root directory, and then it says, Hey, like.
look at this versiongo file. If that versiongo file exists, then
well, if it doesn't exist, just skip it. If it does exist, then go ahead and update it. And what it does is it updates based on a regex.
So another thing we can do is, you know, your approach here is supported. If, like, actually like, the naming of the thing doesn't actually matter too much. So it's more, it's just going to find a regex for this value, and it will update that value there. But yeah, this is this is the workflow here.
My goal is to have it so that this can get overridden, and I have a proof of concept already working. I was working on that right as the meeting started.
But essentially, if you have some sort of
Well, we already have some sort of configuration for this. It's that Versionsyaml file right? And so if you already have a versions that Yaml file all you have to do is really say.
Okay, look in this module. Like, right here, I want to specifically say, like, Hey, this versioning
file exists at this path and just give it a path essentially from there.
You know how that path is. I guess, relative to the root module. Maybe that's yeah. I guess there's like details there. It's details. Also on this file. I have it currently as its own, like
level. Maybe I can embed that in here, still looking at that, so like the actual details of it, are a little bit still up in the air.
But yeah, that's the idea is essentially like you would have.
there's 2 different things I'm thinking of right now. So something, this becomes like a an object. And then you have
something like this. And then, you know, it's something relative.
I don't know can't remember where you got. I think it was something like distro. And then
something like that. Is what I was thinking. And then it also works because you could have multiple places where this could
potentially happen. But yeah, so this is kind of the goal.
**Ron Federman** 11:19 Yeah, that sounds great to me.
**Tyler Yahn** 11:21 Okay.
yeah, like, I said, I've got a proof of concept. I just have to get a Pr up and then popularize it. The Gosig is one of the maintainers of this project, the other is
the Collector, Sig. So I don't anticipate a lot of
any. I don't anticipate any opposition given. This is a no out for files that don't currently support this. So yeah, I think that this is just an added feature. So I don't think there's going to be too much of a problem getting this in. So yeah.
hopefully, Pr, can be up today. If you want, I'll I'll I mean, I'll also link it in the issue or the current Pr, that we have.
But if you want to take a look when that happens, we can do that.
**Ron Federman** 12:11 Yeah.
**Tyler Yahn** 12:14 My question about this milestone is that we did have other bug fixes that were here
like, namely, this one.
It's not being built for arm. Do we want to do a patch release like we have planned here
without this versioning Pr, or did we want to wait a few more days to get this versioning Pr in before we do this patch release. We could also do another patch release. Once we get the versioning in, or even a minor release.
**Ron Federman** 12:43 And I think we can do this this patch like, without the
the version. Yeah, like both the arm
fix and the the well version.
**Tyler Yahn** 12:59 Right.
**Ron Federman** 13:00 Both both of them are regressions.
**Tyler Yahn** 13:03 Right? Yeah, I agree. Okay, I I think that's that's a a smart idea.
So if that's the case, I can work on a
Pr to get a Ver to get a release out this afternoon, if that makes sense to everyone. And I will move this into our next milestone.
Yeah, cause, I think this is probably
yeah. Both both of these things like you said, are regression. So like, let's let's try to prioritize. That probably should have done it more. But yeah, just being busy.
Okay, yeah, I will. I'll try to get a release out this afternoon.
Okay, next up. I'm guessing, Mike, you added this one. This is shifting probe management to manager.
**Mike Dame** 13:56 Yeah. So I met with Raphael last week
and walked him through. This is the the Pr. I've changed the name from process management to probe lifecycle management. So that's the big update. But I kind of going through it with him. I thought that that kind of reflected, a lot more of what's actually happening here. And it looks like I do have some conflicts to resolve. But yeah, he left some good feedback. You know, I basically, the the conversation I had with him is it was
talking about the functionality. We didn't really go line by line in the code because he he was saying, like, you know, I haven't really, you know, Con, contribute any code to this yet. I don't have a lot of background on how the manager works and everything. So I explained, like, this is what it's currently doing.
And this is what I'm changing and kind of what I wanna like, remember, out of that is that the scope of this Pr is actually like a lot smaller than I think we've been making it out to be. I kind of realized that through this talk with him, and kind of like peer reviewing it together.
so this, this change kind of just to reiterate? Isn't
trying to push any sort of probe Api like finalized changes, or really even do much with the Probe Api itself. I'm really looking at the machinery and the internals, for you know how the the like auto instrumentation framework works by shifting some of that stuff from the probe to the the internal you know. SDK, I guess you could call it an SDK or framework.
The main goal with this is just to start chipping away and removing things from the what is right. Now, the probe Api, to kind of give ourselves a bit of a cleaner slate to look at, for you know, what do we want? The final design to look like?
And this is just one thing in that which was, you know, I basically opened up the probe dot go and looked at. Okay, what are some of the internal packages we have imported? What are some of the ones that I can move out of here. And so that's how like shifting the probe lifecycle management. So
I would really like to like with that in mind that this is kind of this is should be a narrow, scoped change. I'd like to push toward trying to get this merged soon.
I think you know, I'd like everyone to kind of keep in mind that that scoping here that you know, we're really just trying to move some functionality. And that, you know, involves changing the interfaces a little bit. But this isn't trying to push towards anything final as much as it's just trying to
remove dependencies from what we have right now. So
yeah, I'd appreciate it if people could take a look at it again. Look through the the changes with that in mind. I I feel like we've gotten a little bit scope creepy. With this pr, so far, you know, some of the manifest changes that I I added.
but just in general, like what we're really looking@isthemanager.go and the probe dot go taking things that load and moving those into the manager.
so yeah, give it a look.
I think if you kind of
take a step back and look at it that way. You'll see that like, oh, this is you know. A pretty small change. That's
we're gonna be iterating. There's gonna be more things like this, I think, but I don't want to try to do too much in one pr. At a time, and kind of intentionally, you know, leave some stuff not perfect at this point in the interest of easier review and easier understanding of like, okay, this is the bigger goals that we're moving this functionality so that we can do more moving, and finally get down to like a clean slate that we can
polish off into. You know something that's external. So
if you have time, I'd really like to get this. You know, we should be able to get this into the next release. It's a pretty small change, all things considered, and it's not something that I don't think anything here is gonna block anything that we're thinking of for the probe Api
And if we get a couple of changes down the road and realize that something does nothing is external, yet we can still roll back pieces of it if we need to. I don't want to do that, but I think that, like I don't want perfect to be the enemy of good in this case, where we're spending too much time on just this very 1st pr, here. I think that we can
iterate you know and and work from there. So yeah,
that in mind. Review it with the the the intent in mind, the scope in mind, and try to keep, I guess. Comments to that scope.
we can talk like in hypotheticals of how this might influence the Api design, but this is really not meant to be a cornerstone change in the in the Api. It's kind of just like carrying water at this point to like, you know, chop would care like
bringing some stuff out of the probe Apis that we can isolate it. And yeah, I I think Raphael seemed pretty on board with that idea. I know in his comment. He was talking about a lot of the future things that we'd like to do with the probe Api and I kind of told him like, Yeah, that's that's all
really like beyond the scope of this. And he he I don't wanna speak for him. But he. He seemed to get that. And I think that this sort of change of moving, you know, runtime lifecycle functionality into the manager will actually make it a little easier for us to expand to those functionalities that he's talking about.
yeah, I'm kind of rambling at this point, but that's just the general, I'd really like to push forward on this. See it for the the bigger picture of of what it is. It's a relatively small change. But yeah, I think that we should be able to get this wrapped up pretty soon and move on to the next one. That's like it. That's that's it for me.
**Tyler Yahn** 20:30 So, yeah, I was looking through. This looks looks good. Thanks for putting this together, working with Raphael talking through this. I like that idea.
the thing that seems very much missing right now is like a north star into like where we're going. And having that documented, I guess
I think I think you're right, like, I think this is a small change, and it doesn't seem to
controversial. I do.
I guess.
No, this isn't it. So we have, like the custom, probe right like issue.
Right?
I have no idea but my thing
that I would I would like to have is some some sort of understanding of like what our vision is, because, like, you're saying like, if this is iterative, if we're just trying to like
chip away at it.
that's good. I think we need to all agree on like the direction that we're going, though, in that in that process.
because it's it's very easy to like. I don't have to say it, I'm sure, like I'm not saying you're doing that here, either, or anyone is doing that, but like
to to flounder back and forth because we don't have a clear vision as to like what those chips should be going towards. Right
and so like, I think that that's that's kind of critical. I want to make sure that like.
because I mean, this is, there's no way. This is up to date I like. This hasn't been updated since the the Bayla donation, right? And so like, I think that, like
honestly, I think that the the North Star here is to make sure that like.
**Mike Dame** 22:07 There's an integration pathway that our probes can be used in in that package as well.
**Tyler Yahn** 22:12 And so I think I think if you keep that in mind, I think what your Pr is doing is in line with that. I think that that's correct in that direction.
I just want to make sure that we have that documented, and clearly, like all agreed on that like.
because I think it helps helps review these processes as well like, if the next Pr comes in and it changes everything you just did back like we could say, well, hold on, that's not really helping. Get us to this North Star.
**Mike Dame** 22:39 And and I think that you know I can make that clear. I kind of have the North Star for at least what this kind of subtask of the probe Api design is, and the other ones that I'm thinking of following up. Or you know, this iterative kind of cleanup. Is kind of, you know. I'm sort of picturing it as like, all right, we wanna like Redo this room. But the room is kind of a mess right now, and so get in and sort of just like.
get stuff out of the room, put stuff onto shelves and like organize it a little bit so that we can actually decide. Okay, now, we see, like, this is the core stuff that we know is gonna be that we haven't gotten rid of that we know is here. And so that that's
kind of the point where I think that our design phase will be a lot easier. I feel like we came into this at the start, and we were really trying to like. Think of all the possibilities. And we were kind of I almost feel like confused, not confused, or like thrown off or thrown in a bunch of different directions. And so that's my goal. Here is like, well, let's take the cruft like the all the messy stuff.
or whatever we can that we agree on like, okay, this doesn't need to be in here now, and just like, give ourselves a little bit of a cleaner slate to come back to the design table and look at like. All right, this is what we have right now we got rid of a bunch of stuff. How is it looking? It's just such a tough starting point that we have right now? And so that's sort of my, it's like a sub
like goal North Star for the main custom probe idea. But I can definitely put that into, you know this thread. I know Nicola and Raphael aren't here right now, so it'd be good to hear from them, sure that they'll, you know, feel the same way, you know. Think it's a fine idea. But yeah, I that's that's kind of what I'm going towards is I'm not trying to push the design so much as like just clear us a pathway to get to the design with this and some other Prs. After it.
**Tyler Yahn** 24:43 Yeah. So this is kind of what my concern is, though, because I think that it could be aligned with with that original goal that I was saying where we're going to share probes across Bayla and this project, but I think it could also be counterproductive in the sense that it is going to clean things up and divide things in a way where it solidifies structure that is not aligned with that.
So I I want to be careful there, because I agree, like, I think a lot of my work in this project has been trying to do that like organization of the room
that you're talking about. But I do also wonder that, like
you know, you can also lock yourself into patterns and designs that are going to structure this room in a way that like, yeah, it actually needs to be a, you know, instead of a square, it needs to be a Pentagon or something like that right? So I want to make sure that, like we're we're cognizant of that.
**Mike Dame** 25:35 While we're doing this.
And I think to that, one of the things that we've come back to a lot is the discussion between like structs versus interfaces and how that and I have a point with this that I'm gonna make. But something that has come up a lot is, you know, we can't expand interfaces, but we can expand structs. And I think the
layout that we have right now where you know the manager is a a struct. And the probe is an interface, and the probe you know, nests that manifest struct that kind of sandwich of struct between the core Api interface, I think, gives us the room to expand what we need to on both ends, where
new functionality, new interactions with probes can be added to the manager in the future, and
new, like identifying aspects, can be sort of injected through the manifest I kind of think of. In this case. The manifest is a little bit of a extensibility backdoor that we have where it's, you know, like our our foot in the door to the Api to say, Okay, if we need to add new stuff without breaking the Api, we do have the manifest. But I I think that that's kind of the the approach. And as long as we have that set up where we have, you know.
we've decided that the manager will be the the entry point, the interface to interact with probes through this framework. And then the the probes themselves, the the core Api should be minimal minimal surface area. I think that these are all consistent with concepts that we've brought up.
I just don't wanna fall back and have us, you know. Still, like like you said, floundering around on, not knowing where we want to go, because there's just so much between us and anything.
**Tyler Yahn** 27:26 Well, okay, but to make it more concrete, like. If I passed a probe with this interface satisfaction into Bela right now, could it use this to to start something.
If it's not going to use the manager, it's going to use. This probe could like it, work.
**Mike Dame** 27:44 Yeah, I mean, you could implement your own manager. I think that that's the idea is you'd have to.
You know your manager would have to act on the probe. So that's
I think part of this is my mentality of thinking that the manager will be the main way that you interact with, you actually use these probes.
**Tyler Yahn** 28:09 But so that's but that's not the case, right? Because, like Bela, has its own like management, processing pipeline that is
redundant, if not like external to the our manager. Right?
So like this is this, is this is my like. This is my question. So like, should
should Bela be restructured to use our manager.
because, like, if that's the case, we have a lot of work to do to support a lot of different functionality, right? Or is the ultimate goal is like the ultimate North star. To share probes across the 2 projects.
**Mike Dame** 28:41 Yeah, I think that trying to make the probe
itself actionable and supportable, like solely independent, is trying to bundle too much into this project. I think that this project should, you know, provide probes as a common Api for defining. And you know this is my static definition of these are the symbols that I want. These are the offsets and the concepts that I need to inject into that in my program.
and then this machinery that we have will actually manage those. I think that that's a better way to do it, and if you want to not use our machinery, you can still use the probe Api and write your own machinery. But that machinery is going to have to act on the probes. Get the you know, collection from it, and probably stuff that you want to do. Anyway, if you're in that scenario. So
**Tyler Yahn** 29:38 But yeah, that's that's like.
that's the the meat and potatoes there, though, is that like that? That? Probably thing that we were talking about just there like, what does that look like? Right? Because, like, if if we're trying to build this probe Api right now, and we're going to change this from a load to an init startup config right like this. This could be great, but this could also be counterproductive.
right like, if the Bela processing pipeline. I mean, they have their own definitions of probes as well, and I'm guessing they look very similar to this.
Not sorry, not what I highlighted, but just to our, to our definition as a probe is like as a whole, right? So like.
I want to make sure that what we're doing here is not something that's counterproductive. Right like. Is this change
moving us closer towards that definition that is going to be universal across our manager as well as the Bayla project, or I'm sorry ob I'm going to start saying Ob, because that's what it is. Or or is this.
you know, orthogonal? Or is this like like this is, this is like the the question I'm trying to get at like this is a concrete example of it, right? Because, like, we are changing this probe definition here. I'd really like it. If we can get
a definition for this probe. Api that we we can agree on in in Obi as well as here, and then
and then all of that other like refactoring things around that interface definition becomes really easy, right? Because if we can work with that interface definition ob can work with that interface definition, and then we can restructure the entire room to be, you know, reduce dependencies, decouple things like that makes a lot of sense to me. But if we do a lot of that decoupling, and it enforces
the structure of this Api to be in a particular way, and that's not conducive to working in the ob space. Then what we've designed is a probe that works for us, but is not going to be compatible in the long haul.
And so like, then we're gonna have to redesign that in in the long haul.
because I think you're right like
having this so that we can, we can expect
the ob processing pipeline to do some sort of like state management and processing and updating, I think, actually makes sense like. That's what I was hoping Raphael would be able to like comment on, because I think if they do that as well, it's just.
you know, I don't know that a hundred percent. So I'm not a hundred percent sure. But like I would expect that they expect to hold state in their processing pipeline. But I just want to make sure that, like what we're designing here is something that they can use, I guess, in the long haul.
**Mike Dame** 32:06 Yeah, and so on that end. I think that my
goal for it would be, have this be as minimal like like I was saying, and we have to hear them way into. But have this be minimal and not very functional. My hypothetical have the manager and the, you know, auto dot new instrumentation be.
Tooling that we provide, and that, I think, gives a good separation of concerns between these 2 things, that our project is providing where you know the you can use probes without having all that extra stuff and functionality added into them.
and if you need more than what is being provided in the pipeline.
Then you can wrap the pipeline. You can build your own ideally.
but I think that we are. It's kind of goes back to like when we were 1st looking at these is like we were when we were talking about. Well, what kind of you probes should, or what kind of probes. Should we support different K probes and network probes? And I think that we'll just. There's so much to support that like we'll overload ourselves, and we won't be able to come to any sort of convergence on anything. So the
you know, logical, and, in my opinion, opposite of that is, make it as minimal as possible. And if you need to build something around that, you can wrap it and import it and build your own logic. But I think that it's too much for us to try to think of every use case that a probe can support. But we can think of more and more use cases in the manager which can expand and grow because that can change without breaking everyone.
**Tyler Yahn** 33:54 Yeah, I guess I'm not trying to.
I'm not trying to go back to designing a general purpose solution here. That's that's not what I'm trying to do. I'm trying to design something that works for 2 systems. Right? Oh, if you step back opens, telemetry has a problem right now, like we have 2 different ways to instrument, go binaries with Ob Project, and with this project and the donation
vision was that those 2 would be unified in some way
it originally was that, like they would take a dependency on this, except
they really don't need a dependency on our management
processing pipeline right? So that that was talked about in in multiple meetings, about this right? So then, the other alternative is, what if we could
unify probe definitions and use them in both projects.
So that was where I'm going with this. So like I'm not trying to say say, like, it needs to support every single use case. What I am trying to say is that it needs to support
working in this project as well as in the Ob project.
**Mike Dame** 34:51 Well.
**Tyler Yahn** 34:51 Think that that's a pretty clear scope at that point.
**Mike Dame** 34:54 I I. My understanding of the unification was that they would take a dependency on this, because.
**Tyler Yahn** 35:02 That's that's been changed. So so I don't like
No, I don't think that's that's the ultimate goal.
**Mike Dame** 35:10 And it.
**Tyler Yahn** 35:14 I mean, I could pull up the the meetings for the ob, but I thought that was like 2 meetings ago. I thought that you were a part of this discussion as well. And so
yeah, I mean, here we we can pull this up.
**Mike Dame** 35:28 Cause. I mean that kind of shit like that shifts the the
way that, like otigos, is also using this too. Right? So
the idea of this being a library that's imported where ob is the, you know, the the open source component that is
implementing this library and using it sure, but other people should be able to build other components off of it, same as the collector has its own framework for writing components and building a collector. There's collector Contrib and the open telemetry collector core project. But you can write your own stuff off of that
same as with. There's the Go Api.
**Tyler Yahn** 36:15 That that hasn't changed, though like that. That's still the goal.
So I I,
yeah. So so this is this is the meeting that we talked about this in in the May 21st meeting.
The the goal here is this custom probe, I think, is, is how I see this North Star, and this is why I want to make sure we have alignment in here. Right? I see.
I see there being an independent package that is hosted here is hosted in my own Github account is hosted in your own Github account. Right? That is an instrumentation probe. I'm going to just say Http, right? Like I've got my own Http instrumentation probe.
Can I take that instrumentation, probe and provide it to this? You know this project, this opentelemetry go instrumentation project, and it can run that probe.
Can I also take that probe? And can I give it to Obi? And it can run that probe
like I want to be able to say yes to both of those things I want to be able to say like, That's that's my, that's my north star, right. And I think that's what I understood. This refactor.
**Mike Dame** 37:24 So I think I think that I misunderstood, and maybe I'm wrong. What you meant by take a dependency isn't Ob will take a dependency on the Api type from here, right? Or is this gonna be
merged? So like, where's the.
**Tyler Yahn** 37:40 Which Api type.
**Mike Dame** 37:42 Probe, you know, if if.
**Tyler Yahn** 37:44 I think it will. I think it will take a dependency on that Api type for the probe. I don't think it will take an Api on the Go Api for instrument, like the new instrument from the auto package. That I think was the original idea. I don't think that's the idea anymore.
**Mike Dame** 38:00 Okay? Yeah. I think that that I mean, Ron, what do you think does that work with the way that
we use it? And cause. It's I'm kind of trying to build like a a base case with that right? We have, you know. This obs, and when you have, like 2 examples, that kind of fleshes out more. What the generic application on Ron. Do you have any thoughts on how that fits into
cause? I don't.
**Ron Federman** 38:29 Yeah. So what I originally like.
as you guys talked about like
and on the original proposal, like, Okay.
it was talked about that the the new project will have a dependency on the go instrumentation
repo, and that makes sense like what? Like the same, as Tyler said, like, you can like it in open telemetry, you should have one source of truth of this is the solution for instrumenting go processes.
So I I didn't completely understand, like
the change in the goal. But if the end goal is to have a
one solution in here, that instrument go processes and another solution there that support go processes. I think that's against the donation proposal. It's it.
It wasn't like the original idea. But maybe I didn't understand that correctly.
Like, if you have a, we have implementation here that does
ABC with you folks on another implementation. There.
I don't think that makes a lot of sense.
**Tyler Yahn** 39:41 Yeah, I I don't either.
but I do think that if you can define the U probes
in a centralized in like a unified Api way, this this idea of a custom probe api and
we use that definition here, and we use that definition in Obi.
I think if that makes sense.
I do think it does open up another question, though, of where?
Where this project's vision, I think, ultimately goes to right
because I see it like this. I see it as
we want to have a unified like single way, right? And I think, like the custom probe thing is.
it's kind of outside of this.
because we also want it to be that like like, Mike was saying, like, we want to contribute model for probes, right? Like, we definitely want it. So that, like 3rd parties can provide their own probes and extend things beyond what maybe the core functionality of whatever open telemetry provides. Like, I think that's that's definitely a needed thing.
but then the question is is like, Okay, what runs those probes? Right? Is it this project? And then ob takes a dependency around the thing that runs the probes in its project? Or is it ob that just runs the probes directly right?
And I think it doesn't make a lot of sense to try to have ob
take a dependency on this project when it already has a multiprocessing pipeline that is is very like targeted at handling specific use cases. And it's, I think, going to get bloated by taking a dependency on the instrument.
I think, taking a dependency on a custom probe Api. That we define here is extremely not only like important, but also valuable, because that that opens up the possibility of you know, probes.
but the thing is is then, you know, this is kind of the discussion during the donation is like we need to still be able to support any sort of project like odigos, or any other 3rd party library that did take a dependency on the instrument
is the idea.
So maybe that's more of a question to you is, if we have a custom, probe api and upstream, you had.
I guess, maybe upstream. Do you have a dependency on the instrument, because if you don't even have a dependency on the instrument, okay, you do. Okay.
**Mike Dame** 42:01 So I mean, I guess that kind of leading into it is A selfish question. Would it be expected for Otigos to, I guess. Take a dependency on ob, would ob be providing the instrument? Or is it? Yeah? So in that case, what we do is we use the instrument. We use a lot of the you know, functionality that we've built in.
Like with resource attributes, since I know that those changed but we call auto dot new instrumentation, new instrument, right? Ron.
And then we manage that at our own level, where we've kind of implemented the manager on top of that. So I think that's where I see the the value of at least having that instrument. And I think
if Obi doesn't want to take that dependency, I wonder what happens with it or I get what you're saying about, like the probe should be able to pass to anything and use it. And that's where I think that
either, using the provided manager that is available using, you know, ob passing it your probes you kind of end up defining like a spec and a standard of like this is a probe. If you're gonna loading one. These are the interfaces that you're gonna get and so if you're building one of these tools. And you want to support hotel auto instrumentation probes you're gonna need to handle it with these steps.
and yeah. So I guess that
we can enforce that in code by putting those steps into the probe which is the opposite of what I did in this pr, so like keeping those interface those functions in the probe kind of enforces those steps.
or just have it be like defined. As you know, this is what to get
it. I think it being minimal kind of
opens up more flexibility to how you work with that by being so.
**Tyler Yahn** 44:04 Don't disagree. I think that I don't disagree either, like I think keeping it minimal is is generally the more valued in in
it's it's the right approach.
It's just the function signature of what those minimal interfaces exist like, what what those are defined as
that, I think, needs to be agreed upon. I think I think that's the more important thing.
Because, yeah, if you if you cut the the function signatures down from 5 to 3, like usually is a great idea, especially if those 3 can encapsulate. All the functionality that you want to like have the core function of a probe do.
I'm all on board right. It's just if those signatures work for the manager, but they don't work for whatever Obi needs to plug into eventually. That's the thing that like I want to like, get ahead of that is is what I'm saying.
**Mike Dame** 44:51 Yeah. And so I think what I'm kind of getting is all we have seen is talk to Raphael and.
Pose these questions to them.
Do you
expect ob to use the the instrument that we have? It sounds like you got. We've already talked about. No.
**Tyler Yahn** 45:12 I don't, but I also I don't know
**Mike Dame** 45:16 I was saying that to Nicola and Raphael. I was
I know that they're watching the recording, and they're answering right now.
so that I think would be the main one.
Yeah. I had kind of a train of thought with that.
**Tyler Yahn** 45:37 Think I think, on that train of thought. Sorry if I'm jumping in, but just like I think
I think that's a gray area to be honest. And I think that there's a lot of question marks there.
But I think that having a probe Api that can interact with it at the manager level or at the Ob level, is not really a gray area. I think that's agreed upon. We want that like, I definitely got agreement from the ob Sig or the
yeah, I'll be sick. Sorry that just sounds funny from the Ebpf Sig that like they yeah. Like, if we have a custom probe Api. They would absolutely take a dependency on that, because
then users can start providing these things we could we could be. This project can also become a library of all of the probes that we have. Right? So like, I think that there's there's not much of a question there.
It's just that we want to make sure that that Api is something they can take a dependency on, I guess. So yeah.
**Mike Dame** 46:29 Yeah. And when I talked to Raphael about this, and I don't wanna speak for him. He seemed pretty into the idea of shifting this functionality out of the probe Api and into the manager. So that I'm just. I missed maybe some conversations, or I'm confused on that maybe he also didn't quite understand where the manager was. He was telling me that he was like, I'm not super familiar with the code base, and so I was explaining the differences between the manager and the probe. So
maybe, like, I definitely understand a bit more. Now where you know the the Ob to epf discussion has been coming from. So maybe there's some miscommunication or or just my misunderstanding there.
but yeah, I think that that's the I. The idea is.
do we want fully functional probes that can like work with themselves and load themselves in in reference to this? Pr, that's what how it's relevant is.
should the probes be actionable on their own, without any other machinery involved? Or should the probes be a static like class definition of this is what I'm going to do, and whatever you plug me into as long as it supports hotel probes.
and maybe it'll support it in different ways. But then it will be responsible for like turning the lights on and making.
**Tyler Yahn** 47:55 Hmm.
**Mike Dame** 47:56 From.
I think that that is a better. I don't wanna say better, but that's the way that I'm leaning towards in this. I think that it's a maybe a little cleaner distinction. But I also, you know, I've clearly gotten some. I've drifted from following the the plan exactly. So maybe I've missed some things, and I'm missing some context but that's where I'm leaning right now.
**Tyler Yahn** 48:22 I don't think you are. I mean, maybe. Yeah, maybe the context is there. But I think actually, you landed on the same endpoint like. I don't. I think, when I was talking in that meeting about the probe design in Obi, I think they also have a very similar
ethos around how to design probes and how they're very simple, and the orchestration exists outside of them. Right? I just don't think that their interface looks the same as what our interface does, and so like.
and I don't think it should. I? Honestly, I don't think that our probe definitions should fully encapsulate the functionality that they may require, because they do a lot of like centralized orchestration for things like trace context, or something like that, like or trace ids or something like that
that maybe we shouldn't. And those could be extensions to the Api like you're saying, like, I think minimal is better right. But like, if you can get like a core set of functionality, and what their management processing pipeline looks like, what ours looks like if we agree upon like what they touch, what they don't touch, and what the probe is responsible for. We're in a good place, and then we could start building, I think, in that direction, and I think they agree on that as well based on conversations, not on research.
**Mike Dame** 49:30 And yeah, and I think from our end remote ago, like, we're pretty simple with it in that as long as we can continue using like the instrument we we don't, I think, Ron, correct me. We don't want to rewrite the instrument, or, like, have our own instrumentation.
We're not planning to that we would like to import, go auto and use that in our tooling. So
this design should I? I think that that makes a case, for maybe not for people that don't want to use ob directly. But do want to use the the probe Api. So it's is this a chain a dependency chain? Or is it like a dependency pyramid that people can take.
**Tyler Yahn** 50:19 Sorry I lost you for a second there.
But my Internet is unstable, but I think from what I heard we were sounding like, we're we're all in agreement at this point. So I think it's more just what are the next steps.
**Mike Dame** 50:30 Yeah, no, I was just making the case, for what otigos is like. Expectations are of this is working with this being able to use. You know, a provided like basic manager for loading and unloading. I think the functionality that we have for loading unloading is great because it's it strips
out a lot of the other stuff that like Ob would be doing and so my question there was, would, is this kind of like a would it be a chain dependency, or you know, with
like a a pyramid triangle dependency? Where like does this go? Probe api to ob to otigos, or does it? Could it go probe Api to, you know, otigos on one side, ob on the other? And
that's I think. Yeah.
**Tyler Yahn** 51:17 I think so. The way I see it right now is, I definitely see that the like more, I guess, in your pyramid example.
**Mike Dame** 51:23 Where it would be.
**Tyler Yahn** 51:26 You know, this probe Api is depended on by the instrumentation via the manager, which is then depended on by odigos, and this probe Api is just depended on by Obi right.
But the thing is is like, I kind of see this as a you know, you could say a pyramid or a wedge right like. So I think once you do that.
having having a discussion on, if we want to try to unify the instrumentation, or the manager after the fact, because I think a little bit easier, because we all agree on the fact that, like it needs to support this, whatever this probe. Api is right. So I think if we can agree on the probe Api, that's a great starting point at least, and it may be the stopping point as well like, maybe that's that's where we all want to land it. But I don't think that that's going to be the case. I think that that's going to also open up the discussion about like, can we unify this into a more centralized place like.
you know, because I think unifying development is a great way to leverage the the community right like this. This idea of like monetization, of like instrumentation is the whole point of open telemetry, and the more developers we can get aligned into the same vision.
I think, is is the goal.
So let's start. I think with the probe Api. I think that's a great great starting point, and like, let's keep it going in that direction.
**Mike Dame** 52:38 Alright. So what do you think is our action item, to to move along because we really want a probe api that we can use that modular idea of having, like probes, be able to be their own modules is it would be great for us. And I'm sure same with ob same with Bayla, too, so.
**Tyler Yahn** 52:57 I think just the observability market in general would be yeah. Cause I think then you get anyways force multipliers that people don't aren't even associate the project and start providing their own right like that's huge.
**Mike Dame** 53:08 Exactly.
How do we? What do we move toward next.
**Tyler Yahn** 53:13 So I the way I see it is like, I don't see your Pr blocked necessarily.
In fact, I think it that it looks fine but I do think that we need to like.
My next step is, we need to get like some
proof of concept that shows a probe from open telemetry. Go instrumentation
that is run in ob like that's the steel thread that we need right like, and if you can do that, then it becomes a lot easier story of like this is eventually how it's going to look. Oh, here's all the problems that like we want to address, or something like that. I think if you can just show that import cycle, even if it's in like a fork or a branch of this project, obviously, it's gonna have to be, because you're gonna have to export
some sort of probe here right in some sort of probably bad looking situation.
I think that's kind of the next step
after. I'm not saying that blocks your Pr at all. I'm just saying like, I think that's that's the 1st 1st step in trying to get a design in that iterative approach that we were talking about earlier.
**Mike Dame** 54:14 Yeah. And I don't want to just merge this Pr, just to say I merged to Pr, right? I want it to contribute something, and if that is, you know, cleaning up a little bit of stuff, or even if if this is just like not something that we're looking at right now, if that's another like 5 steps down the road, I can just wait on this, or to close it, or whatever. But so.
**Tyler Yahn** 54:34 Yeah, I see it as as like getting in.
I see 2 ways like I I think you could close it. I don't know if that's a great idea, because I do think that there are improvements in here that are like
helping clean things up and making things cognitively easier. But I do think, I think, without that other steel thread that we just talked about where, like a probe from here, is getting used in Obi. There's so many unknowns that it's hard to like
to know if this is going in in the right direction, or I don't mean that negatively. I just I just don't know, like I literally don't know.
So the worry I have is, if you do get that proof of concept going, there may be so many different changes that come in in that process, that this Pr becomes irrelevant at that point, because there's just so many like, you know, merge conflicts at that point. So I guess it's up to you. I'm happy to, just, you know. Put this one over the finish line and then go from there because, like, you say, like, it's a cleanup, it's a stopping point we can. We can iterate on it. I think that the next step in the iteration really needs to be. That proof of concept, though, is, is what I would vote for.
**Mike Dame** 55:38 Well, oh, sorry, Ron!
**Ron Federman** 55:42 Oh, go ahead! Thank.
**Mike Dame** 55:43 I was. Gonna say, if it looks salient to you, it's basically a No. OP in in the end goal. So if you think it's good to merge like, approve it or otherwise. If you don't get to it in the next week or 2, we can close it, and we can focus our energy on
getting this proof of concept which we'll need Nicola and Raphael to work on, too. From Otigos. I think the proof of concept is pretty simple because we use the the new instrumentation thing. So if it works
in here, it works for us. And that's what we're planning.
**Tyler Yahn** 56:16 Yeah.
**Mike Dame** 56:17 Right? Right? That's Bio.
**Tyler Yahn** 56:20 Yeah. And I think that's the beauty of the whole thing is like we already have one half of the situation solved right? It's just about the other half now. And so that's, I think.
the the missing piece of information. So okay, that that sounds good. I don't think it'll take me 2 weeks to review this. Pr. I'll give it another look if I don't. If I don't find any like
glaring errors which my quick review didn't show any. I don't see why we can't merge this.
**Mike Dame** 56:42 And like, if it breaks something or we do decide to change stuff, it's revertable. It's not yet. So yeah, I'd I'd like to just get it off my plate and have it. I think that it will logically help a little bit. You know.
But then.
**Tyler Yahn** 56:58 Let's let's do that. I think, then maybe the action item for this is to just capture
this, this idea of this proof of concept, the steel thread in an issue, maybe maybe a new issue, not the custom probe.
But yeah, like a steel thread.
It can be related. Can you create that issue? Or which is that something that I? Okay.
**Mike Dame** 57:19 I I love the idea. I think I get exactly what you're saying. I wanna move this along. Yeah. So operation steel thread is a go.
**Tyler Yahn** 57:28 Awesome.
I'm super excited.
oh, shoot! Ron has to drop. I was. Gonna say, we got 4 min left, too.
Okay, well, we've got the slack channel as well. So, Ron, I'm guessing you look like you were talking to folks. Please go ahead and maybe add those in the slack channel. If you have to drop at this point.
**Mike Dame** 57:48 Yeah, sorry for yapping too much.
**Tyler Yahn** 57:52 It was a good conversation.
I don't. Yeah, I'm all about it.
**Mike Dame** 57:56 But cool. Alright so yeah, if if
I think we know what to do, I'll I'll make.
I'll make operation steel thread and we can coordinate on that. Because, yeah, once we have that proof of concept.
even if it's messy, or you know, just showing that something can be imported and used by them. That'll, you know, show a lot.
**Tyler Yahn** 58:19 Frame. It frames the discussion at least, right like it'll probably show the weaknesses. It'll show the the gaps or something like that, or it'll show that it's 100% compatible already, like, it'll just show things right. I think that's kind of the the goal. Yeah.
**Mike Dame** 58:30 Cool, so.
**Tyler Yahn** 58:32 Awesome. All right. Well, we can end here, then. Thanks for joining.
**Mike Dame** 58:35 Yeah, thank you. Have a good one.
**Tyler Yahn** 58:37 Yeah, enjoy that. Bye, yeah, you as well, yeah.
**Mike Dame** 58:41 Bye.
