SIG: SIG Injector
Date: 2025-09-22
Duration: 74 minutes
============================================================

## Zoom Recording Transcript

Bastian Krol 00:14:01 Hi, folks!
Antoine Toulme 00:14:03 Hello!
How we got Ted today.
Michele Mancioppi 00:14:11 Oh, Ted, what did you do?
Antoine Toulme 00:14:17 You're on mute.
Michele Mancioppi 00:14:19 Who did you punch?
Ted Young 00:14:23 Yeah.
What? Did I make a Prometheus joke here? What do I do?
I'm kidding, I'm kidding.
No, this is why I wasn't… I was actually in surgery during this meeting last week, so that's why I wasn't here.
Antoine Toulme 00:14:40 Oof.
Bastian Krol 00:14:41 That's a good excuse.
Ted Young 00:14:43 Yeah. But I did.
Michele Mancioppi 00:14:45 Probably marginally better.
Ted Young 00:14:47 It was a… it was a really good meeting, actually. I feel like you guys laid out, laid things out very well in that meeting.
Antoine Toulme 00:14:57 Oh, nice.
Ted Young 00:14:57 And I'd like to get that.
Get that written down.
Somewhere.
Antoine Toulme 00:15:03 Ugh.
Ted Young 00:15:04 I'll help, I'll help, seed that dock, cause I think… Yeah, anyways, I have some ideas. I'll put some things on the agenda.
Antoine Toulme 00:15:15 Thank you. Appreciate this.
I felt like we were rumbling a bunch, but that's usually what we do.
Ted Young 00:15:23 Yeah, sure, of course. Same.
Antoine Toulme 00:15:25 You have a concentration of product people in this call, too, because, you know, I'm product now, so I… I'm not paid to talk, and you gotta be careful with me.
Michele Mancioppi 00:15:37 A concentration of what?
Antoine Toulme 00:15:39 product people.
Oh, horrible.
Michele Mancioppi 00:15:41 We brought that people. Yeah, yeah, we are critical mass.
Ted Young 00:15:44 Product engineers were the worst breed.
Michele Mancioppi 00:15:50 I identify as a product person.
And then, as Bastian knows, whenever I feel like, I change that.
Bastian Krol 00:15:59 Yeah, I think that what he was referring to with product engineer, so… Weird hybrid people.
Good!
Ted Young 00:16:12 Yeah.
Antoine Toulme 00:16:13 Awesome.
Michele Mancioppi 00:16:15 Busty, maybe you want to give the good news about the fact that you haven't yet found a bug in my PR?
Bastian Krol 00:16:21 So, so for context, Michele has… done things, not in the OTL injector repository, but…
Michele Mancioppi 00:16:30 Yet.
Bastian Krol 00:16:30 We still have a… have a downstream copy variant offset in our Dash Zero repositories, and… The last hurdle we also discussed here for quite a bit, and… in other, communication channels, is that there's currently some case, depending on how the binary under-monitoring is built, that can crash with the current injector, and we get as done very weird black magic things with ELF and reading file offsets and whatnot.
And I'm currently finishing up that work, so… and the plan is, we want to first.
Michele Mancioppi 00:17:14 You skipped on the part where it's ungodly, but it works.
Allegedly.
Bastian Krol 00:17:18 I thought I made that clear with the black magic term, but yeah. So, yeah, anyway, so the plan is to finish that up. That might take a little bit more.
Of course, there's still some testing to be done, etc. So then we roll it out to our Dashivo customers who don't know it yet, but they will be the cannery in the coal mine, basically.
And after that, when it, when it's… somewhat better tested, we want to also upstream these changes, which… it's still the same ZIG codebase, obviously, but it's not entirely trivial code changes, so it's another big chunk of changes. Maybe not as big as the first Zig contribution that we made a while ago, but still sizable, and yeah.
That's… That will happen at some point.
No commitment, no deadlines from me.
At this point. Or no timeline, let's say.
Antoine Toulme 00:18:27 Okay, no worries.
Michele Mancioppi 00:18:29 But the good news is.
Antoine Toulme 00:18:31 It doesn't matter.
Michele Mancioppi 00:18:33 What the binary looks like.
As long as we can find a lipc in it, we're fine.
And if we don't find the RIPC, we're fine as well, we just don't inject.
Bastian Krol 00:18:45 Right.
Antoine Toulme 00:18:46 Enterprise people with that type of behavior.
Bastian Krol 00:18:49 Yeah, the alternative is to crash the process, which also might sort.
Michele Mancioppi 00:18:54 No, it's even… it doesn't even… it's not like it crashes, it doesn't even start. The linker goes and says, nope.
Bastian Krol 00:19:00 Yeah, right. It happens. So the current binary, when there is one of these rare problematic edge cases, just… you cannot start the binary, so the… the… injector doesn't even get control and cannot even, like, lock something that would indicate the problem. Yeah.
Antoine Toulme 00:19:20 Interesting.
Michele Mancioppi 00:19:21 So this is why I was, So, uncharacteristically skitterish about upstreaming the ZIG injector.
Before finding a solution for this, because the behavior when we found a dynamic process that did not link libc was… A spectacular rock.
Now… it works.
I mean, I don't want to jinx it, but I think it works.
Antoine Toulme 00:19:50 Okay.
That's neat. So, just looking over the PRs we have, we just have some relatively innocuous PR, so just got the stuff from Jack Merged.
Thank you for the fix, Bestie, for DumbCat. I think we're good.
We should just get all the automated renovate boat PRs merged, because they're just standing there doing nothing. I'll just get on them.
And… and then maybe we should talk about making a release, right? We said that we would do something about that sometime.
Michele Mancioppi 00:20:26 Hey, I was asking, pretty please a draft release, so that you can run some, additional… Yeah, of course.
Antoine Toulme 00:20:33 Yeah. Yeah, we should… we should really just… I mean, the other thing is, this is open source, like, what exactly… what… what… sure, we can make it to the draft release, that is not a problem. As many as you like. Any day.
We should make one nightly, if we want to.
Michele Mancioppi 00:20:48 Pretty cool.
Bastian Krol 00:20:49 Don't have 90 changes, so that's a bit…
Michele Mancioppi 00:20:52 The reason why I'm so cautious is that for something that performs the darkest of magics, like the injector.
We should try to make a first good impression.
Bastian Krol 00:21:05 Yeah, that's fine.
One thing about the release is the open PR from you, Antoine. There was a little bit of bike shedding going on with the release numbers. If we do the three, digit or three-number SEMBER style, or just a counter, To be honest, I'm also leaning more towards the very usual, that everyone knows three-digit separated by dots format, even if we don't attach particular somewhere semantics to that, but yeah, I'm also… don't have a strong opinion there.
Antoine Toulme 00:21:47 Yeah, so… okay, we should talk about that, like, let's take this time to talk about it, and.
Bastian Krol 00:21:53 Exactly.
Antoine Toulme 00:21:53 I think this is a really good use of this meeting. So, yeah, you're right, because Senvare is used by many different, repositories across the planetometry. There are some considerations for some there, which are really important for Go, which kind of muddies the waters a little bit about some of it, because, I don't know if you know this, but… once you go 1.0 and go, you can't really, like, remove an API easily, so it has to be there forever. And that's creating a lot of tension inside the collector ecosystem, for example, because nothing can go 1.0 until everything's just, like, clamped.
on the bridge of the Titanic as hard as it can.
So… I really… The thing is.
I would like us maybe to even decorrelate a little bit, because sometimes this is a tendency we have as human beings, is that we tend to have this… we can't possibly do this before we do that, and maybe we could just do a bunch of snapshot releases with whatever time of day it is, or date.
Bastian Krol 00:22:54 Right?
Antoine Toulme 00:22:55 Just so we can get into the actual rhythm of finding out what making release actually entails.
Bastian Krol 00:23:01 Yep, good point.
Antoine Toulme 00:23:03 I don't think it's that simple, right? I would just… I would just say that making release is never easy.
Knowing how to make a really is not easy, knowing how to make that a social exercise with multiple people is even harder.
And we should just, we could even pause this whole version number discussions, or we could just make it separate, so we don't have to have some sort of a… we can't possibly go there until we've done that. It could be that we just decide that we use an absolutely hilarious, bad, release name that makes it so clear that you should never use this stuff in the first place, that it will deter people from using our things, and we can continue to use it for testing.
So… you know, what do you think about, you know, having a release name that's, like, experimental-0001 or something like that, or whatever, like, Experimental-2025-0922, something like that.
Bastian Krol 00:24:03 Yeah, sure, like, a pre-release doesn't sound too bad.
Antoine Toulme 00:24:07 Yeah.
Ted Young 00:24:08 Just for some clarity, like, everything in OpenTelemetry is required to use Simver.
Antoine Toulme 00:24:14 Oh, well, that's… that's it. We're done.
Bastian Krol 00:24:17 Good, okay.
Antoine Toulme 00:24:18 So it's gonna be 001.
Michele Mancioppi 00:24:23 I have an impertinent question.
Ted Young 00:24:26 Yeah, there's nothing wrong with just, yeah, 001 and just sticking to, like, build numbers at first while we're alpha, and then just sticking to minor numbers until we feel like we can release a definition of stability that one… hits. I think it's okay for this… crazy project to explain itself to people, what we mean. When we say 1.0, we're saying we're, like, committed to, like, stability in some hardcore way, but I do think we can define what that means for this thing.
Even the GoSig, right, like, the Go community gets slightly cranky with us, but we do have a slightly different definition.
Than what they… they use there.
Mainly to do with minor additions to APIs.
they say you can't add anything to an API because you might break some dynamic something-something somebody was doing somewhere in Go, and we say, like, that's just a bridge too far for us.
Antoine Toulme 00:25:28 Okay.
Ted Young 00:25:30 you know, with our APIs, we may add a thing, so if you implement our APIs, you need to be aware things might get added, and… because that's just… so, anyways, we can do the same thing with this repo, just to find what it means.
Antoine Toulme 00:25:43 Okay.
Alright, so the other… the point, which I think is valid, which is that our… our releases are actually just a consumption of all the releases that we are building upon, so all the… we end up packaging all the SDKs around here, and we just, you know, put them together, and we hope for the best, and… we've… we've pushed them out, meaning that… I'm gonna say that.
every release we make is dependent on the release of the upstream packages from us, such as another Node.js release is made, we need to release again, right? Am I missing something?
Michele Mancioppi 00:26:21 Well, technically, that depends.
So we have, we have two ways for that.
One is, so actually, it's even… we should even discuss the difference between releases of OCI images and releases of system packages.
With, Debian and RPM, it's relatively simple to actually have different release strains for, for example, the injector versus the Java agent versus the Node SDK with, without the instrumentation, and then make a meta package that actually allows you to pull particular ones. But since there is a common interface, and the fact that environment variables and locations of the files. I think we can pull it off without having to release, for example, a new injector package every time the Node.js releases something.
With OCI images is more complicated, unless you want to end up attaching 6 different init containers, which kind of sucks.
Ted Young 00:27:26 Yeah.
Michele Mancioppi 00:27:27 It would be… Kubernetes version of 31-something has a way of mounting images as volumes, which would honestly help, but it's in alpha, and nobody seems to use it, so it may remain in alpha forever.
Antoine Toulme 00:27:43 You mentioned that. I thought it went to beta in the last release.
Michele Mancioppi 00:27:47 Oh, really? Cool.
Antoine Toulme 00:27:49 Because also, I also think this project should not try to be nice to whoever is in 129 or 123, we should just be very focused toward the future, right?
Well, but, I mean, I think you're making a broader point, right? Sorry, I'm getting into a different discussion.
Bastian Krol 00:28:06 I think, honestly, the first release that we're doing will probably not have any container image as a release artifact, so that is… all of that is basically a discussion for… for later, when we… when we add that capability. I think we first just release the DBN and RPM package, right?
Or… what's the plan there?
Antoine Toulme 00:28:29 Yeah, we can start there. We just push them to the GitHub releases, and they're downloadable, then you do.
Bastian Krol 00:28:36 That would be a good first release, I guess, or first step in the release direction.
Antoine Toulme 00:28:43 super nimble stuff. Like, we just need to try it out, and start to have people giving us feedback, because the worst thing that can happen to this project is that we… we spend another year building a bunch of features and code, and we do a really good job of pushing stuff together, and then… No one knows it exists.
Ted Young 00:29:01 Yeah.
Michele Mancioppi 00:29:02 No, honestly, I don't want to jinx it, but the current state of the injector in the… in the terzero repo.
It's… it's valuable, it's consumable, and if we don't add any features in a year, it's still gonna be good.
So I'm… I don't think we were going to nitty-dally for ages about new features and stuff.
Basic mechanics are nailed down tight, and now I feel what we miss is the packaging.
Antoine Toulme 00:29:28 Okay.
Ted Young 00:29:30 This is really what I want to talk about. I put this on the agenda as, like, injector versus product, and I think it also relates to, like, versioning and everything else, because the injector's just a tool, right? Like, the injector's a mechanism.
But there's a product that we want, which is, like, a unified, holistic experience, right? Like, we want our users to have an experience, and that's the injector plus everything else. It's, like, everything packaged up together in one, like.
You know, push button… Kind of thing.
And, figuring out what that thing looks like.
I think that's… on the one hand, outside the scope of this SIG, y'all were talking about this last week, right? Like, there's this SIG, which is, like, how do we build and maintain this mechanism? But in order for this mechanism to really be useful.
Antoine Toulme 00:30:30 Huh.
Ted Young 00:30:31 There needs to be, like, a larger product vision that… That it's fit into, that the community has kind of bought off on.
And while it's… that's maybe outside the scope of this SIG, I think the people in this SIG are very well positioned to at least define what that looks like, to at least like, define a kind of architectural diagram or something so that we can start getting the rest of the community involved. Because we need their help, and we're also about to put a bunch of work on a lot of other people's plates, right, to get what we want. Python and other.
Michele Mancioppi 00:31:10 I, I feel that the best way we can actually get community, buy-in is when Anton goes on stage on KubeCon Atlanta at the Observability Day, he shows a demo of APT installed that just works.
Ted Young 00:31:26 Totally. But… but we need… we need to pair this with a vision. That's… I really think it's important that when we do that.
we talk about how this thing fits into the landscape with the operator, and the collector, and Obi, and the profiler, you know, and like… I mean, what about the new, like, Rust stuff, you know, getting built on top of, you know, Weaver and everything else, and Hotel Arrow? Like, there needs to be a vision for, like.
there's this one thing you install, and it grabs and brings everything with it and manages it for you. We don't have to have that thing totally built, but I do think when we release… when we release this, when we do a big announcement for this, we want to at least be able to allude to that.
Because otherwise, I'm confused, instead of this next round of stuff we're all building on top of OpenTelemetry, it's, like, everyone feeling like a different part of the elephant right now.
And solving different installation problems, but we're gonna end up with a landscape that's, like, even more confusing instead of less confusing, because now it's gonna feel like there's, like, 8 different ways to install everything.
And we want to do the opposite, right? We want to get everyone behind the idea that there's, like, one kind of golden path.
And if you can't use this Golden Path and, like, you want to do everything by hand or something like that, you can totally do that, but we want… We want everyone to be kind of, like, pushing the same message around installation.
Michele Mancioppi 00:33:02 I would love to say that I see the Golden Path, by the way, nice reference to Dune.
The, it's not gonna be that simple, because… Serverless is always going to be weird, forever.
Like, lambda is never going to be normal.
Ted Young 00:33:22 Right.
Michele Mancioppi 00:33:22 the, most of containers, yeah, could fit together, and then you're gonna have a fatal idea, like.
Antoine Toulme 00:33:31 50 shades of automation between.
Michele Mancioppi 00:33:34 NPMI to just install the injector. That part, yes, but serverless will always be weird. And the browser SDK is always going to be mega weird, so there are, like, the more mainstream parts of OpenTelemetry, yes, I see it.
Open down tree, all in all, across all the SDKs? Probably not.
Ted Young 00:33:54 Yeah, probably we're not gonna be shoving Zig into the browser, but it's more that, like, there's a coherent… you know, if you're using OpenTelemetry, you can be like, this is my environment, and it's like, here's the answer. And if it's a specialized environment, like browser or Lambda, there might be a specialized solution, but, I think it's just important that there's an aspect of this that's bigger than just the injector that involves getting everyone on board with the idea that we're going to automate the management of this stuff.
And part of it is, like, there's a lot of duplication going on, right? Like, you're talking about how we have to do a release every time one of these SDK changes, so there's, like, package management happening here.
Michele Mancioppi 00:34:42 You know, ideally that, the moment that…
Ted Young 00:34:44 Especially with, like, the distros and everything else, it's like, what actually gets bundled up into, like, a giant kitchen sink blob? Does this thing have the ability to dynamically scan and download things in some scenarios, right?
Michele Mancioppi 00:34:58 Scanning and downloading, I would not do, but for example, I expect that after we have our… our debut at KubeCon NA, then there is… we bring the SDKs along, and they… create the DBM packages that the injector will consume.
Ted Young 00:35:14 Right. So, we can…
Michele Mancioppi 00:35:16 If the language can be injected by the injector, it means that the only thing you need to have is the right runtime and the files somewhere on the disk. That is a very nice interface, very nice contract.
Ted Young 00:35:31 Yeah.
Yeah, yeah. But it's just… I think… I guess I just really want to stress, I think we… we don't want to just ship a mechanism and focus on the…
Antoine Toulme 00:35:40 Totally.
Ted Young 00:35:40 We need to… we need to also have some kind of vision we're getting people about. You know, like, there's a lot of flexibility here. I don't think we should ever build tools where you can't get around the one magic tool, right? I really appreciate that in OTEL we build the pieces first, and then we figure out how to bundle them together.
So if you don't like our bundler, you don't like our injector, whatever, it's like you're not… it's not, like, an obstacle to… to getting things done your way, but… but if we don't have that vision, that's… OTEL's just, like, on the cusp of, like, we either… really organize this installation experience, and then OTEL's, like, this great way to do APM and all this stuff, or it's just, like, it sounds nice, but in practice, like, it's… it's… the effort is too high compared to… music.
Antoine Toulme 00:36:32 You get the Hacker News comment. This is too complicated, right? This is where we're getting hacker News.
Ted Young 00:36:37 perceived complexity, right? Even if we solve the complexity, if people perceive it as being confused.
Yeah, you get to.
Antoine Toulme 00:36:45 when it's hiker looking into it, it's like, I don't have to do what now? Yeah.
But, I mean, you're not mentioning also, to me, the biggest promise that we have. This is a vendor-led ecosystem so far.
And this is a stab into the vendor approach, right? Where vendors right now would take all those mechanisms and all that, and they would do their own bundling. And we've decided that we don't think there's value in us having that, being unique to our value, right? So we… open source, push that code, we don't want to maintain it ourselves. We think it's actually much better for us to commoditize this For a competition point of view, but also because of maintenance costs, right?
Ted Young 00:37:24 I think a tragedy of the commons would be better than everyone maintaining this…
Antoine Toulme 00:37:29 in duplication. Right.
My personal belief is that the Tragedy of Commons was written to… make a point that was not real, that actually comments work, and win every single time, and that we would get so much more value out of building this type of structure together, rather than trying to come up with our own clever way of doing this.
Michele Mancioppi 00:37:53 Also, From the point of view of purely, like, the ecosystem observability space, OpenTelemetry being a ready-made product.
that solves the problem of telemetry collection is in the favor of the user. I have spent way too long of my life collecting proprietary telemetry and then not having the resources and the space of mind to actually do good on the data. And I would like very much for the next generation of vendors, including their zero, to live or die by the quality of the insights that we deliver, not about who has the coolest time series.
Ted Young 00:38:29 That's absolutely what we're delivering to people, is like, here's a gift, here's better data than you've ever had, and we're really excited to see the competition, right? We're trying to, like, dump gasoline on the fire, like, hey, here's really, really good data, here's, like.
the slickest installation mechanism you've ever had. This is actually better than last generation proprietary injectors and everything else. And now it's like a real race to see who can, like.
provide the best value for the data. I'm excited for that to be, like, the next… the next round in the, you know, observability market, or something like that.
Antoine Toulme 00:39:09 Yeah.
Yeah, absolutely. And, not to mention the gains in performance that we're getting from, you know, leveraging OTLP, which has a lot better, like… I see a lot of healthy competition inside the ecosystem between, let's say, OTLP, Steph, Auro, all these different approaches to making this type of stuff happen.
Which is, I want us to continue to have those discussions in the open, rather than trying to come up with some way of pony up against the other. So, I mean, to me, this is super important because it shuts down a lot of conversations I don't need to have.
So…
Ted Young 00:39:45 But we already have this thing with, like, packaging, for example. So vendors, right? We want to provide a unified thing, but vendors are still going to want to have their packaged-up distro in some form, right? Because for, like, legal reasons and everything else.
People are gonna reflexively want to say, this… you need to use this bundle if you want support, or that bundle if you want support. I can't support you bundling up arbitrary crap with this injector, you know, for example.
So, we need to think that part of it through as well. There's just some aspects of, like, bundling all of this up from the perspective of, like, how do we provide a thing that vendors then package up and provide support with.
You know, there's just some product-y things we need to think through, and I want to acknowledge it to… it's like… it's like half outside of this SIG, But I think, like, this thing needs to be involved, and needs to be, like, committed to making sure that works, because otherwise it's gonna be hard to sell the injector, right? And so we're gonna be like, the injector is so cool, and people are gonna… I already get it from people, it's like, LD preload's not safe, like, that's, like, some weird old… you know, like…
Antoine Toulme 00:40:53 Meh?
Ted Young 00:40:54 Like, like, the APM people get it, but, like, the infrastructure people are like, why do you…
Michele Mancioppi 00:40:59 Yeah, sure, go into eBPF running as root, see how safe that is.
Ted Young 00:41:03 Right, exactly, like, the EBPF people are pointing at the LD preload people, the LD preload people are, like, pointing at the EBPF people right now, like, like, so there's a… we have to, like, get that stuff clear. We have to get sign-off from, like, everyone that, like, this is the landscape of all the… it's like, I want to see a map of, like, here's all the things we want to get telemetry out of, and, like, here is, like, the golden path for, like, which… which tool we have to get… from each, and here's the mechanism for installing it all. I think if we can show it to people, we'll get a lot more people in the community being like, oh, I get what you're talking about, and if we don't, the only people who are really gonna get it are people who are, like, APM product-y people.
That's just been my, like, lived experience, like…
Antoine Toulme 00:41:51 Vendors.
Ted Young 00:41:52 Yeah. But not even just vendors, just the more APM-y, product-y people at those vendors. Yes, that's true. Who understand how critical this is.
Antoine Toulme 00:42:03 And that's fair. You know, I, going back to your why do we have vendors provide their own stuff.
I think they're… they just respond to the market. There's a need. Some of our customers, they really do want to see the name on it, so they know that they're buying the thing. It's more…
Ted Young 00:42:21 Exactly. It's not arbitrary, right? That's why there's, like, some product requirements Just, like, does the mechanism work from a technical perspective? It's like, can we provide, like, can we check all the boxes that the customers want to see? Can we provide, legally provide, like, support and security guarantees in a way they want to see it? And some of that involves, like, how is… How do we spit out packages that other people can then stamp and be like, if you got this build of it, that's… that's a supported build, and you can check the.
Michele Mancioppi 00:42:55 It is, it is possible to do.
At least in APT, with meta packages, and for example, they would be, like, you can either use the upstream at OpenTelemetry Java, or you get Elastic, OpenTelemetry Java, and whatever, and they all fulfill the same slot.
In the package, it's doable.
In container images, not so much, but that's a different topic.
Antoine Toulme 00:43:23 Yeah, we're not… we don't have to… Solve.
Ted Young 00:43:27 Yeah.
Antoine Toulme 00:43:31 Okay, alright, so, hey, I see you have a doc in the notes. Did you want us to look at that, Ted?
Ted Young 00:43:38 Yeah, so this is just… I noticed this SIG got started without a project file, so this is something we try to do, with every SIG, is to not just have, like, what we call, like, forever SIGs, where it's like, what does this SIG do? It's like, well, they just… Work on some concept forever in, like, some indifferentiated mass of issues in the backlog.
We'd like, you know, every SIG to have, like, at least some basic information written down about, like.
What are the high-level goals they see themselves aiming for? And, like, who… who is, like, staffing that project?
I think most of these questions could just be answered automatically, right? Because we've already created a repo, we already have maintainers and things like that.
So I put this doc… this is, like, free to edit.
I would say don't worry about, like, inventing any information, but if you see any section in here where you can just, like, quickly fill in a blank because you know the answer.
I would ask that you just take a pass at that, and then I can come back in and clean this up, and just get it into…
Antoine Toulme 00:44:54 Sure.
Ted Young 00:44:55 Rico.
Antoine Toulme 00:44:57 We had a healthy discussion on the community project when we made the original contribution, where most people who had a say or stake into this kind of participated. I think we can… just that as a basis for some of that? Is that…
Ted Young 00:45:11 Yeah, I mean, I think the conversation y'all had last week, also, like, it seems pretty clear what, you know… so the main thing is, like, staffing. Like, who… the main thing we want to know is, like, who's committed to, like, doing actual engineering work? That's a thing we want to know in every SIG, so we don't have SIGs where people are signing up to talk, but no one's signed up.
to actually build anything. Shocker, that can happen. So that's just a thing we like to have recorded in the staffing section, is, like, who's… you know, who's maintaining and approving, like, who's… who's planning on… on putting effort into what. And the other is really just, like.
what are the… the deliverables this… this SIG is looking at giving people first, right? Like, obviously we're giving people the injector, but you guys have already come up with, like.
I would say it's like, what do you want to have ready by KubeCon in November, and then what do we want to have ready by OTEL Unplugged in February?
I kind of agree. I would… I feel like February is, like, a more realistic goal for, like, having a bigger product launch.
But definitely getting people interested in.
Antoine Toulme 00:46:26 Yeah.
Michele Mancioppi 00:46:27 The moment we deliver the meta package, I would even focus only on Debian, just because it is the healthiest of the package managers.
We make a meta package.
OpenTelemetry, which includes the injector, Java, and Node.js, which is the current scope of the injector, and all the rest is just monkey work, so it supports some more languages. Like, those two languages, so that we prove it's not a one-trick pony.
It's already the best product launch I've seen in a bit.
Ted Young 00:46:59 Great.
Do you think…
Bastian Krol 00:47:01 Just for clarity, the current packages are not structured as meta packages, they just bundle the injector with the…
Michele Mancioppi 00:47:10 Yeah, I have a pass at that.
Bastian Krol 00:47:12 Okay.
Michele Mancioppi 00:47:12 I'm gonna have a pass at that. It's, it takes a little… Okay.
A little affinity with, with APT, and… I did something similar before.
Antoine Toulme 00:47:22 Okay.
Hey, hang on, Ted, you said that November is kind of cutting in close, but you need to understand we have a talk approved for November. I'm supposed to deliberate on that topic.
And I think we can make it as simple as just like, hey, this, again, is pretty much take your doc and present it in slide format, because that's what we're trying to go for. Create some, some, some, some idea about what it is that we're going… like, how cool this is, how great this is going to help the project and the adoption, and we'll do a little demo, and that's plenty for it.
Michele Mancioppi 00:47:58 Or maybe we start with a…
Ted Young 00:48:01 You nailed it, right? There's, like, you've picked two languages that it can install, right, to prove it's not a one-trick pony, and then the other part is maybe just flushing if we can figure out this discussion around packaging a bit more, and like you're saying, pick Debian, or pick one vector for delivering this package, we're, like.
We kind of think, if you were in this environment, this is what the experience would feel like.
So not trying to boil the ocean, right? Like, giving people, like, one taste in one… In one environment, where we're like, we really think it would work like this.
Michele Mancioppi 00:48:38 Not just Java, and Debian is gonna be a piece of cake.
Ted Young 00:48:41 Yep.
Antoine Toulme 00:48:43 So, I'm trying to do something very dirty, and I will apologize, because this is recorded, and he might watch that recording later, so I'll apologize to him.
A buddy of mine called Jason Plum is a maintainer on Java, or a prover. At least, he's got some say or stake into making sure Java works. And I've opened to him to include him into my talk, because he needs a… you know, we… I want to make sure we… make him come to the conference, really. I need him, very much. And, Well, if he signs up, then I'll make him demo Java.
He doesn't know that yet.
Michele Mancioppi 00:49:21 I, I thought you had Jacob as, You're second on the demo, no?
Antoine Toulme 00:49:28 I don't think I have anyone else on that talk.
Michele Mancioppi 00:49:30 I'm pretty sure he said he volunteered back when.
Antoine Toulme 00:49:34 Yes, but I did not put him down, because I could not anymore.
Michele Mancioppi 00:49:38 Damn it.
Antoine Toulme 00:49:41 Well, yeah, I'm being unfair.
I agree.
Hmm.
Let's see if we can add two.
Michele Mancioppi 00:49:50 We sent… I mean, I will be at KubeCon.
Basti, from their server side, is not.
And do we want to crowd the stage with three, and one in a bright red suit?
Okay.
Antoine Toulme 00:50:03 Are you gonna be in that red suit again?
Michele Mancioppi 00:50:05 Naturalist.
Antoine Toulme 00:50:08 Is it getting a bit, like, I mean, at this point, like, is the elbows kind of working out, or is it just…
Michele Mancioppi 00:50:13 It works like a charm. People actually spot us.
Antoine Toulme 00:50:18 Oh, is it the red? Okay.
Cool. Alright. Are you… you're doing, again, the same, like, big booth with, like, the Formula 1 tire… tire changing station thing?
Michele Mancioppi 00:50:29 Yeah, kinda, yeah.
Antoine Toulme 00:50:32 I'm going to make my whole product team go through that. Like, I'm gonna tell them, look, I don't care how smart you think you are, you're gonna have to go get a demo from them, right?
Michele Mancioppi 00:50:40 I actually would like… I mean, I'm looking forward for the competition to actually, you know, react to that. I thought KubeCon London would be much harder.
Antoine Toulme 00:50:50 Well, we're doing the whole aircraft carrier thing. I mean, we have, like, 200 people showing up in 5 different jumpsuit colors, we're doing fuel refueling, like… no, I'm kidding.
Michele Mancioppi 00:51:00 There's actually one company that did the actual Formula One thing, and that is Dynatrace. They have the logo in one of the inner heirloom on the Red Bull.
Ted Young 00:51:13 I don't think I'm gonna be able to make it to Atlanta, unfortunately. Bummed.
Antoine Toulme 00:51:17 Sorry to you.
Ted Young 00:51:20 But, I'm very excited for doing this unconference in Europe in February.
Yeah.
And if we could do a big announcement in November, it's great, but if we could, by February, actually have… Have, like, the next stage of… Productization as a goal.
Michele Mancioppi 00:51:38 And honestly, it depends how… how well the SDK people play ball. Yeah. Because the natural…
Ted Young 00:51:46 They're actually other…
Michele Mancioppi 00:51:47 First.
Ted Young 00:51:47 At the end of the year, I want to also acknowledge… it's like, it seems like there's time between November and February, but not… not really.
Michele Mancioppi 00:51:54 Yeah, exactly.
Ted Young 00:51:55 Because of the holidays and everything.
Michele Mancioppi 00:51:56 No, ideally, so we go on at KubeCon, and the jaws drop so hard that you can hear the sound, and then the SDKs go up and say, hey, can we take over the OpenTeentry Java package, and we'll maintain it?
And that's already, like, 90% of where we want to be.
Antoine Toulme 00:52:13 Well, you guys are completely delusional. But, okay.
Ted Young 00:52:18 I want to drive that through the spec, you know, the spec sig, the maintainer's call, and all that as well.
Antoine Toulme 00:52:24 Yes.
Ted Young 00:52:25 We don't have to wait for… A conference, the…
Antoine Toulme 00:52:30 No, but, I mean, I love the idea of the unconference in February. I think this is great, I think you're gonna have a great attendance, you're gonna have a good time, and I think this is also something that the SDK folks might really enjoy, is to start to have more meaningful discussions between different SDK languages and all that. So, great. Mop out to you, let's do it.
Ted Young 00:52:50 It'd be nice.
Jack Shirazi 00:52:50 One thing that… I'm not… I'm not understanding here as, with the Docker images that are enabled, that are available for the operator, all have the agents in particular locations. There are standardized locations.
So…
Antoine Toulme 00:53:11 All, all of that should.
Jack Shirazi 00:53:14 should allow us to… to just pull them out and put them into the package, and I'm not sure what… what…
Michele Mancioppi 00:53:21 So, in container images, we can keep compatible with the locations of the operator. When we talk about system packages.
In particular, in the optic of vendors maintaining their own distros, their own builds, it makes absolutely no sense.
to bundle the, for example, the Java agent in the same .deb file as the injector. They can be brought together under the same umbrella with a meta package.
you do APT install OpenTelemetry, and it pulls in the injector, and the Java SDK, and the Node SDK, and a bunch of other stuff.
as separate packages.
Jack Shirazi 00:54:06 Yeah, what I'm saying is that the SDKs have already provided a standardized mechanism.
So everything else is… Separate.
Because you keep coming back saying the SDKs need to take, some control, some effort there, but the idea…
Bastian Krol 00:54:25 We're talking about how the SDKs get… get their deliverables to us. That's what you're saying is already kind of a solved problem, is that…
Jack Shirazi 00:54:37 No, no.
Bastian Krol 00:54:37 No, no.
Jack Shirazi 00:54:37 not specifically to us, I'm just saying that there is a standardized Docker image with a standard.
Bastian Krol 00:54:44 Oh…
Antoine Toulme 00:54:46 Are the SDKs getting into the operator,
Bastian Krol 00:54:50 Yeah, it comes to…
Michele Mancioppi 00:54:53 In reality, we're missing half of the languages in the operator. There is no Python, there is no .NET, Or, yeah, there is, there is now, there is .NET, yeah, there is.
Jack Shirazi 00:55:02 Python is there.
Michele Mancioppi 00:55:03 You don't have Ruby, right?
Antoine Toulme 00:55:05 But not everybody, they couldn't lend it. No, I mean, it's a problem…
Michele Mancioppi 00:55:08 Okay.
Antoine Toulme 00:55:09 Come to an operator sync meeting and watch for the complaints and the bitterness, or frankly, just the… the, the, See, the state of the world sucks, because what happened is that when they did those images.
no one wanted to help them out, like, I mean, why would you, right? If you're a Java guy, and some weird guy comes to you and says, I'm from the operator, he's like, first off, you don't know what an operator is, you don't know what Kubernetes is for some of those Java maintainers. This is too much of a semantic creep to understand between being able to understand what ambience to capture from, you know, ActiveMQ all the way to how your stuff is deployed with an operator is a really big stretch. You need to understand, like, a whole intellectual things. So most Java people know Java very well. The moment you mention Docker, you start to get the look, and when you mention operators, they're out of the room as fast as they can.
So what happened is the operator seek, for expediency reasons, plus just to get by, had to build their own images of all the agents themselves, and have been maintaining them ever since. And they can't take it anymore. It's really difficult, it's really on, like, an… The JavaSig, the .NET SIG have had breaking changes that broke those things, it's been really difficult, you don't know who is it, like, responsible for that, how do you deal with this?
how do you maintain this type of stuff? The operator SIG and its release cycle is last in everything, because they end up with all the problems that are coming from upstream from them, right? The collector breaks their stuff.
their driver secret stuff. Everything is just dumped on them, and the operator has been suffering from that for a long while. I've had a… We had a pitching session, like, 3 months ago on one of the SIG meetings, where we talked about it for 45 minutes, and we came to the conclusion that life wasn't fair, and it was not going to get any better anytime soon.
Ted Young 00:56:57 And this injector project, in a sense, is, like, starting to stick it out to people and be like, no, actually, you're gonna have to care about this, because we're going to create this very standard way to do this.
Antoine Toulme 00:57:08 No operator involved, you could do this on your host.
Removing a lot of, like, these layers of complexity and discussion to the direction that they're getting away with right now.
And we start to very simply, and you can… I mentioned that last week, I was like, I went to the Java contract guys, like, you're offering Java files for download. Who, in 2025, still thinks this is a good idea? And I go, like, well, we do? I'm like, no, people want a service file.
They want to know where the logs are going to be. They want to know, like, what rotation for those log files. Like, you need to help them out. You're not doing that.
And they go, we just know Java, we don't know how to install stuff on Windows or Linux or Kubernetes or whatnot.
Bastian Krol 00:57:45 to be honest, I feel like we are putting a lot of hope to solve… I mean, these… kind of integration problems just exist. They are at the intersection between JVM people and systems people, and that the operator couldn't solve it is… I totally get that. I think it's fairly optimistic to… To have the hope that the injector project is the silver bullet that solves all these integration problems, because the integration problems won't… magically go away, and I'm not sure that SDK maintainers are more incentivized to… to contribute their stuff here, because there's also complexity involved that maybe SDK maintainers do… are not comfortable with, which, like, we… what, you use an LD preload mechanism? What… what the hell is that? So, we could try, but…
Ted Young 00:58:42 You're saying, like, they're… now that we've got this, they're gonna have to do X or Y, and I want to emphasize, they don't have to do shit.
Antoine Toulme 00:58:50 No, they won't. They won't do it.
Ted Young 00:58:52 We have to convince them that… we have to sell them that there's a product vision here, that.
Bastian Krol 00:58:57 And it will be an uphill…
Ted Young 00:58:59 Get everyone involved, and we can say, like, there's a way… we want to avoid what you're saying around the operator, where in order to make this work, there's one centralized team that goes around and, like, cleans everyone's room.
Antoine Toulme 00:59:13 for them.
Ted Young 00:59:14 You know what I mean? Like, it can't work…
Antoine Toulme 00:59:15 Thank you for this.
Ted Young 00:59:17 It needs to be the case where we've presented a mechanism for deliverables, and everyone's agreed this is a good idea, and then all the SIGs start packaging up that deliverable for us, and there's this, like, pipeline for pulling it all in.
Because also, like, how fucking big is this kitchen sink gonna get once we add, like, every fucking library you could install in Python and Node, like, everything, you know what I mean? Like, this…
Antoine Toulme 00:59:45 There seems to be a build mechanism for this thing, too.
Michele Mancioppi 00:59:48 Hopefully, we can take a page out of, Ubuntu there in Debian, where they actually, for the libraries that are either in main or in-universe, they package them separately, and that would work decently for all the instrumentations.
Antoine Toulme 01:00:05 That's what we're gonna have to do, but I think we need a packaging SIG, and so that's what I put up to the Java people.
I made them cry, uncle, until they said, no, please stop, we don't want to do RPMs ourselves. And I'm like, you understand, and I want you to sign this in your blood, that you're giving up this responsibility, therefore you will not come back and complain when someone comes up with opinions about how RPMs are built moving forward.
And say, yes, please get out of my DMs. Okay, no problem. I'm out. I got you. Now, we can do the same thing with Node.js and Python, and then we'll go to the Go people.
Who will give us more trouble than anybody else to…
Bastian Krol 01:00:43 We explained to go, people.
Michele Mancioppi 01:00:44 People have nothing to do with the chapter.
Bastian Krol 01:00:47 Yeah. You can't inject into statically…
Michele Mancioppi 01:00:49 Yeah.
Bastian Krol 01:00:50 I agree.
Antoine Toulme 01:00:50 It's just the fact that installing the Go SDK right now, in the first place, is just a manual app, like… You know, they will continue. It's okay, it's fine. We just… the Go people are good at this, that they are very, very thorough in the spec. This is a… this is just talking about the people, not the language or the… the SIG.
That they are very peculiar about making sure that everything makes sense, which… is good, but I've been away… I've been trying to have a… my whole career has never made sense, and so this is the first time I'm trying to meet computer science people who like to think that things should actually be thoroughly, you know, devised, and I admire them for that.
So, anyway, yeah, I think there's a nascent need for a packaging SIG. The next question I had with Java contributed Trask, has been, Antoine, why don't you go and start a thread on community? Like, go away, and go build that packaging SIG initiative somewhere else. I'm like, great, no problem.
Let me see, I don't have time for that, but sure.
Michele Mancioppi 01:01:50 Wait, wait, wait a second. I thought… I mean, I spoke with Tad a couple weeks ago. I thought there was a packaging sick.
Antoine Toulme 01:01:58 Is there?
Nice.
Michele Mancioppi 01:02:02 No.
Ted Young 01:02:04 Like, it's just packaging. We're just… we're just wrapping things up. No, there isn't a… there isn't a SIG like that at the moment. There's no problem.
Michele Mancioppi 01:02:13 Oh, yeah.
Ted Young 01:02:14 For how to, like, coherently bring all of this stuff together. That's the thing.
Michele Mancioppi 01:02:19 Ugh.
Ted Young 01:02:20 We need to be like, this is the landscape of stuff that everyone needs to install, and here's, like, the map from, like, here's all the telemetry we want to get, and for each one of these things, here's the thing we use.
Michele Mancioppi 01:02:31 So…
Ted Young 01:02:31 And here's the mechanism that installs all of that. We need to present that. And then I would like that thing to have a fucking name, and not just be, like, the hotel packaging SIG thing, and then some weird…
Antoine Toulme 01:02:44 Dude.
Ted Young 01:02:45 Based off of that, like, it would be great to be like, this is…
Bastian Krol 01:02:48 Just to be clear, because that topic comes up in this working group, or in the SIG a lot, this is outside of the scope of this very concrete program.
Antoine Toulme 01:02:58 Really is it?
Bastian Krol 01:02:58 This injector should be a small part, maybe some glue part in that larger initiative and context.
Ted Young 01:03:08 But who in OpenTelemetry is the most well-motivated?
To… to convince everyone to, like…
Michele Mancioppi 01:03:16 Grab somebody from Rat Hat, and they do RPM.
And then, maybe I talk with my friends at Canonica, maybe they… they pitch in a little bit on some of the things with packaging, maybe… We can also kickstart it, but I promise you, if the SDKs do not take us… do not take ownership on the fact that.
Ted Young 01:03:36 Whateverish package doesn't break.
Michele Mancioppi 01:03:38 Then it doesn't… this doesn't work.
Ted Young 01:03:40 Completely agree. It has to be… this has to be, like… I really feel like step one there is just to get a bit of a product vision together around, like, this is all the shit that has to get installed, it has to get installed cleanly, this is what traditionally happens to install this.
And, like, this is why, like, hotel's gonna lose in the market unless we do this, right? Because these are, like… these kind of installation tools we're building are actually kind of table stakes.
Antoine Toulme 01:04:11 I agree with that.
Ted Young 01:04:12 market, you know.
Michele Mancioppi 01:04:13 Well, that depends. I mean, there is a whole bunch of our competitors that don't have them, and they thrive.
Ted Young 01:04:18 I mean, like, what we can… however we want to spin it, but to my mind, it's like… like, we have to… to actually be best in class, if OpenTelemetry's gonna be just as good of an experience as anything else you might find out there, we need this.
Antoine Toulme 01:04:34 That's the problem, is that OpenTelemetry came with a promise that we were going to solve the problem of telemetry from applications.
Ted Young 01:04:41 Yeah.
Antoine Toulme 01:04:41 do that, then we're not solving. So, back to Mikuli's point about, oh, yeah, but others are fine. Yeah.
Ted Young 01:04:48 How can we focus only on this problem, and then somehow do it worse than what other people are doing?
Antoine Toulme 01:04:54 Yeah, let's…
Michele Mancioppi 01:04:56 There are… there are precisely two companies that can do the stuff that… The injector does.
So I would not say it is that dramatic, but I see your point on the fact that we should raise the bar. Yes. I think solving it is dramatic, maybe put it that way.
Ted Young 01:05:13 muddling through and having to, like, with this box of Legos is normal. I agree, it's not… that's just the normal thing, but if we solve it, we can kind of make a big splash around that, and that addresses, like, the main concern we hear about OpenTelemetry, which is too fucking complicated and too hard to install.
Antoine Toulme 01:05:31 That's what I want to get to, yeah. I think, yeah, I mean…
Michele Mancioppi 01:05:35 This is a phrasing I can get fully behind, yes. Including swear words.
Antoine Toulme 01:05:42 Yeah, it's too fucking complicated, I agree with that. I mean…
Ted Young 01:05:45 You can't… you can't expect people to understand how OpenTelemetry works before they touch it for the first time.
Michele Mancioppi 01:05:51 Okay.
Ted Young 01:05:52 Right? Like, there's a chicken-egg thing, where if you want to install it, you have to know like, architecturally what it is and what it's trying to do, and of course that's gonna be a terrible first experience. I mean, I do not understand why or how, but a lot of people out there do not have observability as their hobby.
Michele Mancioppi 01:06:09 And…
Ted Young 01:06:11 Yeah.
And open telemetry, because it's flexible, it makes it worse, right? Like, we have all these providers and, like, all this extra stuff, and it's great that we have all of these things, but it's bad that we expose it to people before they get To actually see the data coming out of their application.
Antoine Toulme 01:06:30 you know.
Ted Young 01:06:30 It's like, step one is, like, there's data. That should be step one.
So, I'm excited. I think we're gonna do it. I just, I'm… and I'm gonna try to do my best to make a stab at some of these docs, and just be wrong on the internet, and you all can correct me, and then we can start pulling in the GC and TC, and making a…
Michele Mancioppi 01:06:57 And…
Ted Young 01:06:58 pitch… pitch at… pitch at the community about this. We can do that in tandem while this SIG is just focused on… on building the injector.
Michele Mancioppi 01:07:06 And it would really help if we get on board the Red Hat people.
Which are conspicuously absent from this thing, because their expertise in packaging is pretty handy.
Ted Young 01:07:18 So…
Antoine Toulme 01:07:20 Yeah, we're talking about Peville and, maybe Ben, right?
Michele Mancioppi 01:07:23 Yep.
Antoine Toulme 01:07:25 So, besides this effort, by the way, so just FYI, like, folks, I think you should know this.
I've been driving since February with Red Hat on making sure we have a unified experience for the operator, which is going to be very similar to what we're having in terms of discussion and objectives for the product.
And so, for this particular view of the operator, the problem we've had with our customers has been that the operator just tells you that it's installed for you to support installing collectors and target allocators and other operator-managed resources, but it does not actually tell you how to make that work.
Like, now you're writing YAML.
That's your… that's your life now.
So we have a work-in-progress PR, which I need to get open this week, from one of our engineers, who's going to add a opinionated version of what you should do on OpenShift.
Pretty much, you install this stuff, you give it a destination for your data, and it will install all the collectors on all the nodes.
Install a cluster receiver. It will configure all those things properly.
And you'll start to have much more of a product guidance moving forward.
Meaning, we know what is the best practice on Kubernetes. We know this, we know what to do. We know what control plane metrics you want. We know what they should look like. We know how you're going to get your logs. We know how to do that in a programmatic way. We don't need to have a discussion with you about how you're going to get those logs, but not those logs.
And so we're going to start to do that, and I just want you to see that conversions. It's just… community's much easier, because it's a finite space, there's no Windows discussion, none of that crap and all that. For a host, we need to be more composable, for better or worse, but for what it's worth, this is the direction that we are taking as our impact on the podemetery.
Because we don't see… the impact is not to go wide anymore, the impact is just to make it so that people go from 0 to 5 minutes, like, completely done.
Ted Young 01:09:22 And I think there's, like, deduplication.
that needs to happen in this process, right? Like, there's… how do we install… there's the operator that wants to provide this experience for Kubernetes, like you're saying, but then we also want to provide this experience outside of Kubernetes.
So we would deduplicate there. There's also control plane and configuration management and op-amp.
Right? There's, like… how do you deploy this stuff? And then it's like, now we have config files for everything.
Antoine Toulme 01:09:52 Yes.
Ted Young 01:09:53 Right? And we have OpAmp, So how is, like, the control plane aspect relate to the installer aspect, because that… That has to be a sane relationship as well.
Antoine Toulme 01:10:05 You can throw in Ansible Puppet Chef Salt in there as well, just for fun.
Because these are also participating in that view. So I… I think having a separate SIG for that actually makes sense, because I don't see… I actually think it will be a waste of talent of our SDK people to learn the intricacies of installing at scale this type of stuff.
We need to have a very finite boundary, and the injector actually provides us the integration testing that we needed to make sure that things work the right way.
And so the… I think the injector is going to be providing some level of a buffer to tell us, okay, we know this version of Java, Node.js, Python, whatever, works the right way. And then we'll… we will use that as a part of a Debian RPM story, but then after that, how you configure and make this whole happen, so people don't have to do any… install without leaving OpenTeMP3 I.O. needs to be kind of coming together. So that's the plan. That's what I want us to do.
Ted Young 01:10:58 I think we can make another SIG for this, but also, I plan to, like.
really run it out of the specs. Like, the main… community meeting we have is the spec slash maintainer meeting, and…
Antoine Toulme 01:11:12 Totally.
Ted Young 01:11:13 Yeah, sooner rather than later, I plan to start beating a drum there.
as well.
Okay. Even before… I don't want to wait to get another SIG spun up. I want to take a shot at at least just getting an architectural diagram.
So that everyone who doesn't have this knowledge that we have can at least go… See, like, these are all the different pieces we're trying to bundle up.
These are all the different pieces of work that we have to divide responsibility up around packaging and everything else, just so everyone can be like, we're all… we can all agree it's an elephant, and we're not just, like.
Touching the individual pieces.
That's true. I think we can get the community together. If we don't, yeah, it's gonna be, like, everyone with their own little bit of knowledge talking past each other.
And it's gonna seem really confusing.
Antoine Toulme 01:12:08 It'll be interesting to see if we, So when you talk in Feb, like, we… I think the next, the next meetings we have should be just preparing what the agenda of that discussion you want to have in Feb. Let's imagine you have a room full of maintainers and people who care about the implementation SDKs.
Ted Young 01:12:24 Yeah.
Antoine Toulme 01:12:25 I think we should be able to set some requirements for them so that they can help the injector, and specifically, I would be looking to see if we can have some level of integration testing happening at the injector level, or even some level of acceptance testing. No, we're talking product.
And this is bigger than the injector, right? This is this new SIG, or whatever, it could be just a central repo.
But that might mean that maybe they change the way they release. Maybe they need to do RC releases moving forward.
Ted Young 01:12:54 The short-term practical goal of that doc, I think, should be to present the SIGs we want to work with, with what we want them to be producing for us.
Antoine Toulme 01:13:04 Hmm.
Ted Young 01:13:05 Right, and to the degree to which maybe the operator or somebody else had taken over producing those things for them, maybe, like, that's the short-term goal, is to farm that stuff back out.
To where it's supposed to be in the community.
Just starting with the two languages, you know, that we want to do first. Like, see if we could come up with a vision and then get those two languages shifted over to releasing artifacts in the way that we think Divide the responsibility up better than where it's currently at now.
Nice.
Antoine Toulme 01:13:46 Gotta run.
See you next week. This big greedy's.
Bastian Krol 01:13:51 Next week, I'm out, just… just putting it out there, so I'm not here next week.
Antoine Toulme 01:13:58 Well, let's make sure it is Risa, Bestie, and then assign all the bugs to him.
Bastian Krol 01:14:02 That sounds great! Fair.
Michele Mancioppi 01:14:07 Bye, folks.
Bastian Krol 01:14:08 Enjoy your time.
