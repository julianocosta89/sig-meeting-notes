SIG: Packaging SIG
Date: 2026-06-25
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado Pimentel** 06:59 Well, hello, Michele.
How's it going?
**Michele Mancioppi** 07:07 All good. I'm putting the finishing touches to the presentation I have today, having Claude Creating the slide slides for me in slide dev, and it's an experience.
**Diego Hurtado Pimentel** 07:19 Oh, so…
**Michele Mancioppi** 07:20 Dots.
**Diego Hurtado Pimentel** 07:22 Wow.
Yeah, that guy can't do everything, right? I mean…
**Michele Mancioppi** 07:26 Yeah, if you find the right tools, and you hold them in remotely the right way, AI can do almost everything, yeah?
**Diego Hurtado Pimentel** 07:33 relief.
**Michele Mancioppi** 07:34 It's gonna be interesting.
**Diego Hurtado Pimentel** 07:35 It's gonna be our next therapist, or chef, or… I don't know.
**Michele Mancioppi** 07:41 Actually, there are people that are trying to do therapy with AI, which is a terrible idea.
No, it's.
**Diego Hurtado Pimentel** 07:46 Whoa.
**Michele Mancioppi** 07:47 You would not go to… you would not go to a therapist that is affected on auto-completion.
**Diego Hurtado Pimentel** 07:55 The, sorry, the therapist, that is what?
**Michele Mancioppi** 07:58 That is effectively an auto-completion on steroids.
**Diego Hurtado Pimentel** 08:01 Yeah, I mean…
**Michele Mancioppi** 08:02 There is a bit more to therapy than that.
**Diego Hurtado Pimentel** 08:05 Oh, totally. But… I don't know, man, like, the… AI used to suck.
**Michele Mancioppi** 08:14 Yep.
**Diego Hurtado Pimentel** 08:14 And that… that's something that can be said about AI in pretty much… pretty much every domain that… it has been used, right? I remember the years ago, this meme of this William Smith eating pasta meme, you know.
that it was such a mess, because AI created this video of And, And, you know, the generated images with people with extra fingers and stuff like that?
**Michele Mancioppi** 08:44 Hmm.
The fingers under sand is still an issue, but…
**Diego Hurtado Pimentel** 08:49 Still an issue?
Oh, well, then.
AI sucks then, man. I haven't said anything.
**Michele Mancioppi** 08:56 I think that, like every tool, one needs to put some judgment and some discretion in where to use it and how.
**Diego Hurtado Pimentel** 09:04 Yeah. That's the…
**Michele Mancioppi** 09:08 Hi, Ted.
**Diego Hurtado Pimentel** 09:09 That's the problem with human beings.
**Michele Mancioppi** 09:11 Yes. I mean, if anything has the potential to make all of us more intellectually lazy than we already are.
Which is bought.
Sadly.
It's a thing.
**Diego Hurtado Pimentel** 09:23 already doing.
**Michele Mancioppi** 09:27 Alright.
**Diego Hurtado Pimentel** 09:28 It's too… We're all here.
**Michele Mancioppi** 09:32 I know, I know, Sina, Sina, Sina said, Frank Anniker said, he cannot attend.
Antoine is on vacations, Denise, not sure.
Let me ping him.
**Diego Hurtado Pimentel** 09:54 Hey Ted, sorry, I haven't replied to you yet, I think.
The gRPC issue, you asked me.
**Ted Young** 10:02 Yeah. Yeah, it was just, if you were coming back full-time, it was just seeing… If that was something.
Oh, yeah.
**Diego Hurtado Pimentel** 10:10 yeah, we don't want to…
**Ted Young** 10:14 Yeah, go ahead.
**Diego Hurtado Pimentel** 10:16 Sorry, yeah, we're trying not to… Use extra dependencies.
On the injectors slash packaging, because… Python dependency management sucks. It's not like Node, where one component can have its dependency, and another component has They tend to clash.
the ideal solution will be to fix Python, but that's a little bit out of scope for this project, I guess. So, we're just getting rid of dependencies, yeah.
**Michele Mancioppi** 10:50 And so… my favorite gripe about Python, right? That, the AutoPixporter.
relies on protobuf and gRPC.
**Diego Hurtado Pimentel** 11:00 And then, yep.
**Michele Mancioppi** 11:01 Number one most toxic dependency in existence… in existence in that ecosystem.
**Ted Young** 11:07 Yeah.
Yeah.
**Diego Hurtado Pimentel** 11:09 Welcome to that.
**Ted Young** 11:10 Like, JSON, using JSON for the time being.
**Michele Mancioppi** 11:13 That is one thing, but, the, I mean, JSON is more wasteful, right?
And, doing it in Jensison we eventually want to do as well, but most SDKs have actually their default.
to be, HTTP protopuff.
And, so having Python work with HTTP protobuf, without requiring users to, to change their settings, that is, of course, something very desirable. So, Diego is, looking into effectively implementing the OTL exporters not to depend on gRPC.
**Ted Young** 11:49 Perfect.
Yeah.
**Diego Hurtado Pimentel** 11:51 Yeah, we have a… a pure Python implementation of Protob that we have been developing. Just yesterday, I started, Working on the performance, Testing. We expect at least some other results.
So we probably will need to, implement this.
in, I don't know, Rust or C, or something actually fast, right? But I will keep you updated.
**Michele Mancioppi** 12:21 run that, please.
**Diego Hurtado Pimentel** 12:22 together.
**Michele Mancioppi** 12:23 I mean, also the, I do not know of many applications that are using Python with expectations of great scale and performance.
Don't do that space.
The, having it as an opt-in package, if we see that the overhead is not absolutely atrocious, is a starting point in the injector, and then to upstream it in the, in the Python SDK, I think that requires, of course, more work.
**Diego Hurtado Pimentel** 12:59 If someone complains about bad performance in OpenTelemetry Python, I'm just gonna recommend that issue to be closed. That's your fault for choosing Python in the first place.
**Michele Mancioppi** 13:12 In Python, it's convenient. Let's not slander people just because we don't like their programming languages.
**Ted Young** 13:20 Something that, Alex, Bowen's been working on, right, is, like, a C wrapper.
Right? Like, calling out to the C++ implementation instead, you know, through foreign function calls. Have you all seen any of that work?
**Michele Mancioppi** 13:36 I've spoken with Alex about it. I, don't know where it is. I generally very much welcome the idea of replacing as much as possible of internals of SDKs with a common foundation. My guess was that it would cause a project to rust.
I know that PHP tried it, had some problems with internal strings, and if we actually do it with a C++, with me…
**Ted Young** 14:02 Yeah, I think the C++ implementation of OpenTelemetry is just more mature than what's going on in Rust. That's… the main reason I would look at that.
But I wonder about, like, our… for Protobuff, whether it's, like, the same thing, right? Like, can we lean on what's going on?
for Proto and C++, or is that the same… dependency issue that we're seeing in Python.
**Michele Mancioppi** 14:26 It would require much more rework, because now you need actually to to have the API at the level of, of the exporter.
And, to match, particularly the… so… replacing half of the SDK, like, from the tracer inwards, is going to be simpler than replacing the… Something at the very fringe, like the exporter, because the shape of the, the arguments that you pass between Python and C are different.
And, the ABI for something like invoking normal methods?
No problem.
having effectively read internal representation of spans in Python match what the C++ compiled version of the exporter does.
Oh, boy.
Yeah. It's more like I feel that replacing just exporter It's likely not gonna work nicely.
**Ted Young** 15:25 The current, like, gRPC protobuf, dependency that we have that's causing all those problems, does it have a C component to it, or is it all native Python?
**Michele Mancioppi** 15:39 the GRPC and protobuaff have themselves, three components, but, The problem there is that the library doesn't even try to be remotely backwards compatible.
**Ted Young** 15:51 Yeah, I know.
But… Rather than re-implement things in Python, is it possible to just… Copy, paste into just… no, it's harder than that.
**Diego Hurtado Pimentel** 16:06 To sort of copy-paste what?
**Ted Young** 16:07 I mean, like, their issue is, like, it's two things. They keep breaking across versions, right? And so people can't install OpenTelemetry because we have a dependency, and the Python dependency manager says you can't do it. But if we just made our own fork.
The proto stuff that we needed from them.
**Michele Mancioppi** 16:29 Yeah, but then you're on the hook for maintaining it. It's, I would, I think we can keep it in the… as an idea, if we see that the PurePython implementation is horrific in terms of overhead.
Otherwise, I would rather, see if, Alex or Clint.
Because that leaves us in a much healthier state, I think.
**Ted Young** 16:52 Okay.
**Michele Mancioppi** 16:53 Like, trying to do yet another halfway thing.
**Diego Hurtado Pimentel** 17:01 we could implement this in Rust, and apparently there's good integration between Python and Rust. I just reviewed a PR from Herring049, I think that's Lucas.
Who implemented, something, I just… I have trouble memory.
Rust.
And, it's integrated in Python now.
**Michele Mancioppi** 17:29 I feel that if, as a project, we decided to move towards using a common core for the SDKs, which, again, it's an excellent idea.
then, which language should be something discussed at Infinitum in the TC?
Because that is a high level of rework, and then we need to make sure that you don't have massive regressions across SDKs for the UMB Pro version 2.0 of most of the SDKs.
I mean, that'll be amazing.
**Ted Young** 17:59 Because we have API and SDK separation, I think anything like that wouldn't be… you know, you would just have the existing maintainers and existing SIGs continuing on, and you would do work like what Alex is doing to… To see about, like…
**Michele Mancioppi** 18:13 You know what?
**Ted Young** 18:14 you'd just be spinning up a new SIG that maintained… because it should be possible to do that with, like, not a hell of a lot of work, right? Because you're… if you're picking something that's already maintained, like a C++ SIG or the Rust SIG, and then you're just maintaining the foreign function layer in the different languages.
**Michele Mancioppi** 18:34 Yeah, but I think we're discounting here the subtle incompatibilities and differences in implementations of different SDKs.
For example, which SDKs implement the entry bit?
Yeah, so there is, I would not say, oh, it's as easy as last rip out. I think that there's going to be a lot of… a lot of learning about all the bugs that people have come to depend upon.
**Ted Young** 19:02 Yeah, I mean, it would be… you'd be… what got supported in the configuration file would be different, right? It would just be a… a swap-in in each language. But I mean, in terms of, like, the effort across the project.
you know, it could be… it could be a separate SIG, basically, that was looking at maintaining these foreign function layers.
**Michele Mancioppi** 19:23 No, I think it would be an excellent idea. And then we can really optimize it, and effectively the overhead of OpenTelemetry now becomes a single line, and not, yeah, depends on the language and stuff.
**Ted Young** 19:36 Yeah.
**Diego Hurtado Pimentel** 19:37 Michael, a question. So, How important will be… just imagine that we live in an ideal world where we can just fix and implement things in an instant.
If we could, what would we need to fix in order to have… to put that idea in place of a… of a common SDK implementation, regarding to… how incompatible… how… the difference between implementations in languages. If every language implementation was completely uniform.
Would we be able to do that?
**Michele Mancioppi** 20:17 Yes, I mean, the, all the problems with architecture binaries are all solved, and most languages nowadays have very civilized and performant ways of calling into… into C.
Especially now that Java has actually, I think they made a new version of JNI, and I heard very good things about it.
That is… That was the biggest holdout.
But… What, what kind of things we're going to learn the hard way.
I cannot begin to say. I just promise you that there's gonna be a whole bunch of things where we're going to look at each other and say, wait a second, how could we not notice we implemented X in 5 different ways across 6 different SDKs?
Because that's the reality of things with, very complex projects like OpenTelemetry. It just happens.
**Diego Hurtado Pimentel** 21:09 Okay.
**Michele Mancioppi** 21:10 Anyhow, this is a hell of a tangent.
Another thing that we have, Denise.
Did you have any luck, trying to port my POC to OBS?
**Denys Sedchenko** 21:24 Sorry, I was quite busy this week. I'm basically still work in progress.
**Michele Mancioppi** 21:32 the, I have presented the POC in the maintainer SIG.
I think we are at a point where, we need people to try it.
A lot.
And, I have, logic.
To, publish a version of the packages.
to, Git pages in our repo.
Where… If I have it right, it should… you should be able to point EPT and YAM to it.
But before we go and press the, approve button and publish it, I have the feeling we should, We should feel that the specification for the metapackage architecture is solid enough.
And I've gotten some feedback about it, but… Not to my satisfaction.
Quite frankly. I have the feeling that a lot of it is a factor and tested still.
**Denys Sedchenko** 22:34 And regarding GitHub pages, I assume the packages are basically unsigned.
**Michele Mancioppi** 22:41 Yeah, it's just gonna be a toy thing where you need to turn off signing.
**Denys Sedchenko** 22:45 You know?
**Michele Mancioppi** 22:46 And it's just a point there, and it's downloaded in the big blobs for the repo packages, but at least you have the feeling you can start playing around with APT.
It's technically already usable today, if you build the packages locally, and then point APD to a local directory, which I did on Tuesday.
But, I don't think enough people are going to try it that way.
It's still a bit, a bit too raw.
if we made, like, insecure packages, and you can actually try it via APT, then maybe more people will get it. But also, I have the feeling we need to start making noise in the auto blog about it.
the, after the presentation from the other maintainer SIG, I expected some language maintainers to reach out.
Which did not happen, so we may need to, put it on their radar harder through end users.
**Ted Young** 23:50 I think going to the different SIGs will also help.
**Michele Mancioppi** 23:58 So, in Italy, I would say, to do the… to do the circle of the seven churches. We go through the… the language seeds and then present how it works.
**Ted Young** 24:12 I… yeah, I think that it would help us if we went to the different language SIGs and… and actually, like, encouraged them directly to use it. Also, like, encouraging end users directly to use it. So, like you were saying, the closer we can get to just unsigned packages in a… You know, in a manner that's kind of as close as possible to the final form of it.
It'd be helpful.
**Michele Mancioppi** 24:38 I would appreciate if somebody else in the SIG would actually go and play around with the packages a couple of days before we merge and create the GitHub pages.
That would give me a better feeling. I'm a bit paranoid about first impressions on a technology like this.
There is a lot of magic in it.
**Ted Young** 25:08 Of the language sakes, which one should we go to first?
**Michele Mancioppi** 25:12 The ones that we support are Java.NET, Node.js, and Python.
**Ted Young** 25:18 Yeah.
**Michele Mancioppi** 25:18 For Python, we have Diego here.
for, I actually reached out on the channel to the PHP people, because I run a couple of quick checks, and actually, I think we could provide a decent experience relatively easily. I reached out on the channel and not heard yet.
Yeah. Ruby, We have Matt Ware.
Pursuing the, supporting the injector.
**Ted Young** 25:47 Okay.
**Michele Mancioppi** 25:47 So… java.net, Node.js.
**Ted Young** 25:54 So maybe Node.js is the one Daniel Dyla and them, we should reach out to, just because Node's weird.
Right? And…
**Michele Mancioppi** 26:02 Not more than others.
**Ted Young** 26:04 Oh.
I… I always feel like… There's extra weirdness that comes with Node, but at any rate, that might be the… if we're gonna say, hey, we have a super beta thing, it might blow up in your face, do you mind giving it a shot? Maybe Node.js is the SIG we could reach out to and say, please play with this. So I can poke Daniel Dyla about that.
And see what they want to do.
**Michele Mancioppi** 26:27 And what about talking with Trask for Java?
**Ted Young** 26:31 Yeah, yeah, I can let Trask in.
**Michele Mancioppi** 26:32 The rest of Jack in the USC, and I expect this is on his radar, although he may have the hands full with, The auto operator and the injector at the moment.
**Ted Young** 26:42 Yeah, yeah, I was thinking, you know, like you're saying, like, just… if… if we poke everyone at once and they all report the same bug, that's not… Right, so you were.
**Michele Mancioppi** 26:53 I mean, I did test the stuff, and in this circle, we should do more testing before we go and poke more people.
That's why I have, like, 2-3 people to try to break it.
Get Claude, try your clothes to break what my clothes did, let's see what happens, right?
**Ted Young** 27:10 Fair enough.
**Michele Mancioppi** 27:17 So I would say, first, I get two people to say, in these rooms, to say, I tried 2 hours to break it, I didn't.
And then, the round of the seven churches it is.
**Ted Young** 27:32 Sounds good.
**Michele Mancioppi** 27:35 Good.
And if you had… Yeah, that's interesting. So, we are very committed to, to have a presentation at Observatory today about it.
I understand, so I… I don't know how far we went to this. I think Antoine submitted something and invited me.
for it.
But I also feel it could be something on the maintainer's track.
**Ted Young** 28:03 The maintainer's track tends to be more just giving, like, a project overview.
Cause it's, it's, it's a relatively short presentation.
Like a project update, here's, like, our roadmap. We tend not to do, like, demos and things during that. We'll definitely highlight it, of course.
**Michele Mancioppi** 28:22 It's, okay, then, let's see if it goes through the CFP.
It will be a nice continuation, because we had a talk about it in, London, and then we had one in Atlanta.
with, Jason, Plum, and Antoine.
And, I don't think… I don't think we spoke about the injection system packages at, In Amsterdam.
But if we do it in Solid City again, then, it's a good trumpet.
**Ted Young** 28:58 Yeah, and if there's… the CNCF is, because we're graduating, you know, they are interested in looking for making time for us, so if there's any extra places you can see in their schedule, like other things where we could kind of slide stuff in, that's… that's always an option.
**Michele Mancioppi** 29:16 You mean in other, co-located events, or in KubeCon itself?
**Ted Young** 29:20 No, I mean in, like, KubeCon itself, so if they… if we don't get into Observability Day, we could try to poke them to add it as a lightning talk, or, like, something.
**Michele Mancioppi** 29:28 Yeah, Antoine and I submitted a full talk.
Yeah, I don't think I can submit another one, because I already have two submissions.
**Ted Young** 29:39 Yeah.
**Michele Mancioppi** 29:40 But, for example, if you submit a lightning talk, And then… add me or Antoine to that, that also works.
Cool. Yeah, they got, last time I got a very nasty email because I submitted too many things. I don't want to be banned.
**Ted Young** 29:57 Fair enough. But I'm hopeful that they'll accept your talk, I guess is what I'm saying, is I think they're trying to emphasize things. The CNCF is kind of a big, clunky organization, so who knows, but…
**Michele Mancioppi** 30:09 Nope.
It would be a good way to reach a bunch of users, and I'm very optimistic that when people look at it, they are going to want to try it. For example, when we spoke in Salt Lake City, I had a few people from large European enterprises.
One of the Michelin, they came around and said, not all heroes wear capes. I mean, this is something that is resonating with the system administrators.
A lot.
**Ted Young** 30:42 Yeah, no, it's gonna be really nice when we land it. I think people are gonna really appreciate it.
you know, combined with the Kubernetes work becoming something where you don't have to touch things anymore, and it can work everywhere, that's gonna collectively be a very big step up in people's getting started experience.
**Michele Mancioppi** 31:02 Alright, then, peeps, go and try it out, break it, let me know.
And if you don't manage to break it, then I go around and present it to anybody who would listen.
And some who will not.
**Ted Young** 31:16 Thanks, Michaelie.
**Michele Mancioppi** 31:19 Cool, and then we give each other back 7 minutes.
All right Best is useful in the next.
**Bastian Krol** 31:27 Yeah, exactly.
**Ted Young** 31:30 I have to go to the browser SIG, so I won't be in the injector SIG, but you'll be fine.
**Michele Mancioppi** 31:33 Salter is effectively running a bit on autopilot right now. It's, it's solid, proven tech.
Maybe, Diego, you can come to the… to Injector SIG and show the… the proof of concept with, With Python?
**Diego Hurtado Pimentel** 31:46 Yeah, actually, I… I had just added this to my calendar, so I was planning on… Awesome.
**Bastian Krol** 31:56 Deal in 6 minutes.
**Michele Mancioppi** 31:57 Here's one. Bye.
**Bastian Krol** 31:59 Bye-bye.
**Diego Hurtado Pimentel** 32:00 Hey, who wouldn't want 6 minutes?
