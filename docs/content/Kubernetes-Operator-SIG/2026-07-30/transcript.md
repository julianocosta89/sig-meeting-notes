SIG: Kubernetes Operator SIG
Date: 2026-07-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 06:23 Hello.
more people than I expected after the change in Zoom links, actually.
We could put this on Slack, too.
**Israel Blancas** 06:34 To be honest, I went first to the other call. I was like, oh, yeah, they changed it.
**Mikołaj Świątek** 06:57 How's… how's stuff going?
Israel, are you actually using the HTTPD instrumentation?
**Israel Blancas** 07:11 None of myself.
**Mikołaj Świątek** 07:13 I am excited, because I'm not sure if anyone's using it. Maybe if you know someone who's using it, maybe they… maybe we can try and, like, update it a little bit, and try to get it more on par, because we haven't updated in a long while, and that's because we're afraid, because they have some weird… Support policy that just, like, drops older versions or something?
It should be a breaking change for us.
**Israel Blancas** 07:41 It seems that somebody's using it, because I got the request, so… For it, right? For the instrumentation thing.
Without the CRDs.
**Mikołaj Świątek** 07:55 I guess, I guess if we… if we go through the change to require the instrumentation.
image in view and beta, then it's gonna solve itself.
And everyone can set whatever they want, we just have to publish the images, and that's it.
**Israel Blancas** 08:17 Something that actually we can do is, like, that thing that we're talking today, writing the ticket, we're creating a meta… 2, right? Under… Meetings.
pumping up.
Thank you.
Well, from there, right, like, trying… to maintain, right, the image. They're.
**Mikołaj Świątek** 08:39 Yeah. I'm sorry, but it's like you're cutting out a little bit. I can only understand every second word.
**Israel Blancas** 08:48 Sorry. That's why I was shocked.
Yeah, sorry, I was thinking about the… the thing… the thing about creating the meta ticket, right? The meta issue for that thing, because I know that it's something that we have talked about.
But I guess it's not, like.
public, right? It was more something, like, we talked here, or something, right, in a couple of comments, but it's like, there is not something where we can tell the people, hey.
**Mikołaj Świątek** 09:15 It's because… it's because… It's a little bit rude to write a ticket saying, we want to… to foist this off to a different SIG without first asking for their opinion, I guess is why it doesn't exist. And, like, nobody asked, like, the Python SIG, officially, to… whether they want it.
So maybe it's okay to… maybe you could… maybe it's possible to write that issue in, like, a kind of a general language, where this is not necessarily implied, I think. But this is, like, a political problem, it's not a technical problem, really.
The .NET… the .NET people already own the .NET part of it.
And I am, like, the .NET and Java model is about, like, as far as I'm willing to accept.
for new things, where it's… they go like, here is an artifact, download it, put it in a Docker image, and you're done, right? That's okay.
I am incredibly not okay if this image is, like, our Python image, where there's a whole bunch of packages in there, and if somebody came up, opened an issue, asked, why is this package in here and not this other package that I would like? I don't know how to answer that question.
There is no reason that I know. So that's the situation I want to avoid having in the future.
**Israel Blancas** 10:38 I was asked, for instance, why we are not shipping with the Python auto-instrumentation libraries, the auto-instrumentations for everything AI and AI, right? That now, I think… I guess they even live in a different repository and everything, right?
Bye.
**Mikołaj Świątek** 10:52 The answer to all of these requests should be, please ask the Python SIG to publish something, and then we will use it.
very happily, I will very happily get rid of our own. And hopefully, with the view on Beta 1 changes, and with the injector change as well, it's going to be much easier to just build your own, because with the injector, it's kind of just like… You really just have to have the files in the image at the right spot, and that's basically it.
That's it. Your image has to have a copy binary in it as well, which is stupid, but until, like, image volumes are in every Kubernetes version we support, we kind of don't have a choice.
But otherwise, it's supposed to be, like, if your instrumentation supports… if the injector supports your instrumentation, then, you know, that's basically everything that is required, technically.
And that's it.
Pavol marked himself as being here, but he's not here, so he has lied in the meeting notes.
Tsk, tsk. It's been… it's already been, like, maybe he's in the wrong, wrong, Maybe he's in the wrong Zoom room and wondering where everyone else is.
**Israel Blancas** 12:24 Maybe.
**Mikołaj Świątek** 12:30 There he is.
**Pavol Loffay (Red Hat LLC)** 12:35 Very well.
**Mikołaj Świątek** 12:36 Hey, were you in the wrong Zoom?
**Pavol Loffay (Red Hat LLC)** 12:39 Exactly.
**Mikołaj Świątek** 12:40 I was about to write to you on Slack, yeah.
**Pavol Loffay (Red Hat LLC)** 12:49 I was waiting there, and I felt it's, like, summer vacation time, so everyone is out.
Yes, I remember.
**Mikołaj Świątek** 12:57 I put myself… I put myself in the… I put myself in the attendees ahead of time, and I saw you put yourself in there, so, you know… I think we can get started. I don't know what's happening to Jacob. He's probably, like, on vacation or something.
I've seen Bene be active recently, but I don't know if he's coming to this.
**Pavol Loffay (Red Hat LLC)** 13:22 I don't know if I can dig in properly.
**Mikołaj Świątek** 13:25 Do you have anything you want to talk about? The instrumentation stuff?
**Pavol Loffay (Red Hat LLC)** 13:30 So I submitted two PRs, one was merged, the first one was the initial ghost tracts without the declarative config. It was essentially the cleanup from the B1 alpha one.
so pretty uncontroversial, and now there is a second PR that, adds the conversion, just the internal package that will handle the conversion without the webhook and without changing any Kubernetes configuration, so it's not putting the V1 Beta 1 into bundle, it's not configuring the conversion backlog, anything like that. It's just the internal code, so please take a look, review. There is one thing, it's related to Jacob's comment.
In the instrumentation B1 Beta 1, The… we have removed… the… environment variable setting, or field. So, in V1 Alpha 1, users can set arbitrary environment variables in a couple different places in the CR. In the roots, and then parallel language.
And so… I have removed it.
it completely from V1 Beta 1.
or not completely. I have moved it Into… under the nthconfig struct.
Because the n config kind of provides the… the way to configure SDKs via an environment variable, so we have to have a way how to, kind of, users can set additional configuration. Let's say for the auto-instrumentation.
So it's there. What it means is… To fully support the conversion.
We need to somehow store this information somewhere if the user was setting the environment variables, let's say, in spec.java.env.
Because right now, we don't have it in the P1 beta one, so, I put it into annotations.
So there is an annotation in D1 Beta 1 that will… store this information from where this is coming from, so it can be… converted back to V1.
Alpha 1 properly.
please take a look on the PR, I think it's, It's well… it's obvious from tests.
**Mikołaj Świątek** 16:45 I'm gonna take a look tomorrow. I'm a little bit swamped with stuff.
all sorts of directions, but I'm digging out… digging myself out of it today. I'll be there tomorrow, too.
Mmm…
**Pavol Loffay (Red Hat LLC)** 16:59 Yeah, no problem, thank you. And so, once that's in, I will continue… Oh, and… might continue… Looking at the label selector, We wanted to migrate from annotation to label selector, so that's on my list.
Ends… I will as well probably… maybe help Tyler on the default images issue.
We're going to get rid of the default images.
I'm not sure if Tyler has started, but it's, yeah, it's in the scope for our work as well, so I can take a look at that.
**Mikołaj Świątek** 17:41 Yeah, that's probably not gonna be, like, super… a lot of work, necessarily, I think. It's just… there's some… there's a process that you need to define, and I think that's the majority of what you actually need to do in there.
There needs to be a way in there to… to have something like a changelog? Because, for example, I can see now that, right now, the update to the Python auto-instrumentation image is failing, and it's failing, I think, because they deprecated one of the, or removed one of the packages that we were shipping.
So that's, like, an example of something that has to go into the Python instrumentation changelog, the image changelog.
That this was removed.
And as an example, other things that might go in there are, like… the Node.js image is also failing, but that one's failing because of tests, and it's failing the tests because it actually switched to the new HTTP semantic conventions, so that's another thing that we have to, like, explicitly handle. We can either explicitly handle it the same way we did for Java and .NET, or we can… Just wait with this upgrade until we dials out, and then just tell the user You set, set, set whatever image we want.
**Pavol Loffay (Red Hat LLC)** 19:09 there's…
**Mikołaj Świątek** 19:09 Yeah.
**Pavol Loffay (Red Hat LLC)** 19:10 If there is nothing else, I have maybe one topic that I would like to discuss. So, we… At Red Hat, we maintain, kind of, additional tests for the operator that kind of verify that a bunch of hotel components work with the operator, even though there is no integration for them in the operator codebase.
we are… because we support them, and we need to kind of catch if there is some change, and I wonder if there is Any thoughts or any appetites to have such a test in the operator?
Repo directly in the upstream.
**Mikołaj Świątek** 19:57 What do you… what kind of test is that?
**Pavol Loffay (Red Hat LLC)** 20:01 It's a smoke test for… A component with some default… some config.
**Mikołaj Świątek** 20:09 Why… why is… why does that need to be tested? Like, if the operator doesn't interact with it in any way, then… then… what is the game?
of that.
**Pavol Loffay (Red Hat LLC)** 20:21 Yes, I think… In most cases, Those tests pass.
there used to be maybe some changes in the components that they would start requiring, kind of, additional RBAC, and They would fail.
So that's one example. Absolutely.
**Mikołaj Świątek** 20:42 So the… You mean, like, so it's a question of, like, there's a component, it doesn't… it's not supported by the operator in the sense that the operator sets the R back automatically, but… But you still want to have, like, a config that shows what RBAC is required for this, for your specific configuration to work, is that right?
**Pavol Loffay (Red Hat LLC)** 21:10 For instance, yes.
**Mikołaj Świątek** 21:12 Correct.
I think we could have that. I don't know if I want to run this, like, on every pull request.
But we kind of do want to have guides for specific functionalities, and we've recently merged the first one, which was the OBI one, right?
And those guides should… Also, big tests.
maybe not tests that are, like I said, run on every PR, but they should be testable in some sense, and you should run it sometimes, at least.
So, I'm not totally against in that sense, but it also depends on how many edges there are, because, you know, Contrip has a lot of components, for example.
**Pavol Loffay (Red Hat LLC)** 21:57 Exactly, I think it makes… sense, at least in the context of the operator, to test the Kubernetes-related components, right, that somehow interact with the cluster.
If we… if that…
**Mikołaj Świątek** 22:09 Right, if we… those we should actually just support, I think. If there's, like, a list of Kubernetes-related components we don't explicitly support, then we should just support them. I am super… I am very… Very fine with that.
**Pavol Loffay (Red Hat LLC)** 22:29 Yeah, I think so. We could maybe run this test as part of the, like, upgrades.
And when we bumped the… Collective versioning, because that's when we will see regression.
**Mikołaj Świątek** 22:44 We should configure Renovate to bump the collector version the moment it's released in the releases repository, and not wait until we do the actual Operator release. That should be simple now.
And then, when the collector version changes in the PR, we can run a whole bunch of other tests.
to measure the compatibility. That sounds like a good idea to me.
And then we could also run a whole bunch of, like, tests for all the guides that we have showing all the, you know, how to do… how to configure file log receiver in Kubernetes to get container logs, right?
These are all things that we could run, if we don't have to pay for it for every normal pull request.
So I guess the answer is yes. Under these conditions, I am… I am in labor.
**Pavol Loffay (Red Hat LLC)** 23:43 Yep.
**Mikołaj Świątek** 23:44 Okay, a couple…
**Jacob Aronoff** 23:51 Sorry, I was on mute. Yeah, it… Can you repeat the question? I got distracted with reviewing Pavol's Pure.
**Mikołaj Świątek** 24:02 Pavol, we were talking about, like, doing essentially more extended compatibility testing between the operator and the collector.
So, by which we mean, like, take a bunch of components and have, like, what's the right way to call it? Like, some example configurations on how to do certain things, and turn that into a test, and actually run the test. But don't run it on every PR, because it's going to be really annoying.
Yeah, run a… just do the collector bump separately, as in bump the collector version in versions.txt, do that in a separate PR from the release, which we should do anyway, ASAP, it should happen as soon as the collector is released.
I thought we had dinner.
**Jacob Aronoff** 24:54 I thought you added that automation in, like, months ago.
**Mikołaj Świątek** 24:58 No?
**Jacob Aronoff** 25:00 That's what I remember seeing.
**Mikołaj Świątek** 25:01 Sure, I haven't done that. That part I don't.
**Jacob Aronoff** 25:03 No, I was thinking of the nightly tests that you added in.
**Mikołaj Świątek** 25:07 About 90 tests are different. 90 tests run against contract 90.
**Jacob Aronoff** 25:10 No, I know, I…
**Mikołaj Świątek** 25:11 rigs.
**Jacob Aronoff** 25:13 I conflated the two.
It looks like, by the way, we do have some nightly test failures.
**Mikołaj Świątek** 25:21 They, they fail with, like, some regularity.
**Jacob Aronoff** 25:26 Either way.
**Mikołaj Świątek** 25:27 Time's fine.
**Jacob Aronoff** 25:27 I think it's a good idea.
**Mikołaj Świątek** 25:28 What's up, yeah.
**Jacob Aronoff** 25:29 I think we could run them as part of the night lease, though. No?
**Mikołaj Świątek** 25:33 We thought of… they could also run as part of the night base, but I thought that, We should have.
**Jacob Aronoff** 25:40 Maybe that's too cute.
**Mikołaj Świątek** 25:42 just have a separate PR updating just the collector version, and then run all the… let's call them the compatibility tests.
**Jacob Aronoff** 25:51 Yeah.
How do we decide what, configurations would be used for testing, and what the criterion would be?
**Mikołaj Świątek** 26:00 In my mind, it's like… This should be one-to-one with guides on how to configure stuff.
And we have a guide how to configure OBI.
And that guide comes with tests.
Those tests right now run on every PR, but in my opinion, they're, like, the first candidate to move it out.
**Jacob Aronoff** 26:22 Yo.
I mean, it seems reasonable to me, I think… I would just worry about… the, like.
Scope of what we would accept to be in there.
And making sure that we're not biting off more than we can chew. I want to avoid, like, the thing that we have with instrumentation as well, where, like, we are the… we are the defense line for finding their bugs, you know what I mean?
**Mikołaj Świątek** 26:49 I mean, for instrumentation, we don't really find their bugs.
This one's pretty okay.
**Jacob Aronoff** 26:54 Well, we… I mean, the compatibility stuff is more what I mean for that.
**Mikołaj Świątek** 26:57 It's more that there are breaking changes, yeah, other than bugs.
**Jacob Aronoff** 27:02 I just… I think that we should do the… we should maybe just scope to, like.
A certain type… a certain, stability minimum?
Or something, so that we can guarantee… something there. I would just worry if we go… With one of the ones that's, like, more experimental, That it would break us as well.
**Mikołaj Świątek** 27:27 Yeah, I do agree that if we're going to host configurations, then there should be… they should be for components which are reasonably stable.
**Jacob Aronoff** 27:36 Yeah.
What was the failure here?
**Mikołaj Świątek** 27:43 Okay.
**Jacob Aronoff** 27:43 Probably not.
**Mikołaj Świątek** 27:44 Sorry.
**Jacob Aronoff** 27:46 Sorry.
**Pavol Loffay (Red Hat LLC)** 27:48 What's it?
**Mikołaj Świątek** 27:49 I was going to ask if you're… Happy with the outcome of this discussion.
**Pavol Loffay (Red Hat LLC)** 27:58 So, my understanding is that we can test the components that are related to Operator or Kubernetes-specific.
like, no filter processor, or… I don't know.
What else, like…
**Mikołaj Świątek** 28:14 Yeah, things which are really…
**Pavol Loffay (Red Hat LLC)** 28:15 energy.
**Mikołaj Świątek** 28:16 We reasonably could have some relationship to the fact that you're running in Kubernetes.
**Pavol Loffay (Red Hat LLC)** 28:22 Yep.
**Mikołaj Świątek** 28:22 I would also accept, like, file log receiver.
**Pavol Loffay (Red Hat LLC)** 28:26 Well, this will…
**Jacob Aronoff** 28:26 yards.
**Mikołaj Świątek** 28:27 We already have a time for color this year.
**Jacob Aronoff** 28:29 Gates Attributes Processor would be useful as well. That one is probably the most weird one that I think people rely on.
That one's, I think, particularly odd.
But…
**Pavol Loffay (Red Hat LLC)** 28:44 events, objects that you see there.
Things like that.
**Jacob Aronoff** 28:47 jump.
**Pavol Loffay (Red Hat LLC)** 28:51 That sounds good, I think it will.
Make our life easier.
**Mikołaj Świątek** 28:56 It won't make our life easier, to make our users' lives easier.
**Pavol Loffay (Red Hat LLC)** 29:01 And…
**Mikołaj Świątek** 29:02 our life harder. I mean, it will make you as in Red Hat?
**Jacob Aronoff** 29:06 That's fine.
**Mikołaj Świątek** 29:07 Easier.
**Pavol Loffay (Red Hat LLC)** 29:10 And so we agree as well, running these tests only during the Operator upgrades, not… on all the years.
**Mikołaj Świątek** 29:17 And maybe, maybe nightly.
Like, it's, it's my… it's, it's, it's… good to get.
**Jacob Aronoff** 29:24 I think we should do them nightly… Yeah, and I also think we should do them with, We should also do them with the collector upgrade automation. Yeah.
Cross.
**Pavol Loffay (Red Hat LLC)** 29:38 Yeah, I think that should block the collector upgraded example.
**Jacob Aronoff** 30:06 It looks like Obi failed on the overnight, is what the issue was.
**Mikołaj Świątek** 30:14 Should Obi succeed on Contrib?
It's not the contribute image, right? It's something else.
But it should be the same test in that case, because it uses a different image, so that's just, like, flakiness from main.
**Jacob Aronoff** 30:33 Yeah, I'll send it here.
**Mikołaj Świątek** 30:37 Anyway, I add, like, two things.
Yep. One is that… I don't know if you read the thread on the Leeds channel, but… If you recall, we've had this intermittent… these intermittent attempts to get rid of BusyBox from the instrumentation images.
**Jacob Aronoff** 30:58 Yes.
**Mikołaj Świątek** 30:58 Because CVEs and blah blah blah blah blah, BusyBox, we only need BusyBox to be able to copy something in that image, and there were, like, attempts to replace it with, Rust core utilities with a Go handwritten Go program that copies.
with…
**Jacob Aronoff** 31:18 Yeah, I remember.
**Mikołaj Świątek** 31:19 some Amazon thing, and what I did as an experiment was basically… just inside the Docker container, just download the official tarball of GNU core utils.
And just build the copy binary from that.
**Jacob Aronoff** 31:40 Is this, maybe I'm conflating two things. Doesn't this go away with the injector? Like, the… I mean, we'd still have to build the injector container.
**Mikołaj Świątek** 31:48 No, no, no, it goes away with image volumes, like.
**Jacob Aronoff** 31:51 The image volumes, that's right.
**Mikołaj Świątek** 31:52 The reason we need this is that all of the content needs to be on a shared volume with the actual application.
That's the reason, and that image volumes address that.
But other than that, we need the copy frame.
so… and I did that, and you get, like, a… 100 kilobyte binary that just does everything you need, and builds for every single architecture under the sun.
So, I am kind of seriously considering publishing an operator Docker image, which only has that one binary in it, so we can use it in the build process of all of our instrumentation.
This is really stupid. It feels incredibly stupid, but I can't… Finds, like, an actual… technical, obstruction to it. So I'm bringing it up. Maybe you can tell me a reason not to do it.
**Jacob Aronoff** 32:55 I mean, I think it sounds good. I'm happy… I would be happy to get rid of, BusyBox, And I think it would be good to get rid of that, honestly. I think that we would just have to think about the maintenance burden and make sure that, like, Renovate can update any security stuff on it.
**Mikołaj Świątek** 33:14 It's like, you literally key it from the upstream release of the new CO2 tools.
**Jacob Aronoff** 33:22 Okay, if it's that simple, I think we should just go for it. Previously, we were worried…
**Mikołaj Świątek** 33:26 it's not even, like, a distro package, it's literally their published… the upstream projects published hardball, and yes, Renovate can actually… because they have a… like Linux, they have a GitHub mirror, so you can… you can see their releases as releases in GitHub.
So, so, like, Renovate handles this very, very easily.
**Jacob Aronoff** 33:49 Yeah, then I think there's no reason not to. I mean, I'm trying to think of anything against it, and it's just another image for us to maintain, but if you're saying that the maintenance burden is low, then I think we can take it on.
**Mikołaj Świątek** 33:58 It looks pretty low, like, the… the Docker file is, like, 20 lines, and it essentially just downloads the tarball, unzips it, and just, like, runs make configure, and then whatever command is there to specifically build the copy binary.
And that's it.
Runs perfectly fine on all the architectures we support.
The only reason I want to have it… the only reason I want to have it in… a separate container image is that it kind of takes long to build in QEMO, and the reason it takes long to build is that there's kind of a…
**Jacob Aronoff** 34:40 Virtualization, right?
**Mikołaj Świątek** 34:42 I mean, that's not true.
That's not really the main reason. It takes longer to build than you would expect naively, but it's not actually the building part that takes the time, it's the configuring the build system itself of whatever they are doing. You have to configure the whole build system to build any of those binaries, even if the binary itself you build in, like, 5 seconds or something.
So, I don't want every instrumentation image to have to do that on its own.
Hmm.
And that's why I want to publish a separate, separate one.
But I would… I would like to explicitly mark this image as just internal, not for use for anyone, breaking changes at any time, you know, don't rely on us. Don't rely on it.
**Jacob Aronoff** 35:31 I think it sounds good to me.
**Mikołaj Świątek** 35:33 Okay. I might open an issue separately, or maybe just pull up the pull request and show it.
I was surprised that this worked the way it did.
The other thing I had was… I… yesterday, I merged a pull request that adds a package containing helpers for integration tests written in Golang.
We already have some of those. They've been added because, as part of the standalone target allocator work.
There's a test, it doesn't use chainsaw because it doesn't use the operator at all.
It just uses the customized manifest, and it installs target allocator and checks a bunch of stuff.
And now we'll be able to write more of those tests. My first candidate test for this is gonna be… I put the link in the document.
My first candidate for this is going to be the target allocator Prometheus conformance Test, where you, like, literally Spawn a bunch of stuff, a bunch of service monitors and applications, and then collect the data using both the, target allocator with Prometheus receiver and the Prometheus Operator plus Prometheus F, and you assert at the end that both of those give the same labels on that data.
**Jacob Aronoff** 37:01 Yup.
This is great.
**Mikołaj Świątek** 37:03 want to do, and I'm not gonna write it in Bash, so it's gonna be written in Go. You gotta, you gotta parse some stuff. And I also have, like, a highly vibe-coded, but also kind of straightforward port of a bunch of our current tests in Chainsaw, which use a lot of Bash into this framework, and they're much smaller in it.
**Jacob Aronoff** 37:24 Yeah, I like that idea. I especially like the idea that we don't have to do a lot of the coordination. I think as long as we're using weights correctly.
To avoid any races, that… that's the only thing that would have… That I think would be problematic.
Because we've had a couple of.
**Mikołaj Świątek** 37:39 Totals.
**Jacob Aronoff** 37:41 Good.
**Mikołaj Świątek** 37:42 We're using what? I didn't understand the word.
**Jacob Aronoff** 37:45 Like, race conditions. The benefit of chainsaw is that it gave, like, a nice… way to do… wait for this Kubernetes condition to exist, to continue.
**Mikołaj Świątek** 37:58 Yeah, well, it's pretty straightforward.
At the end of the day. You don't have to… in these tests, you typically don't wait for as many things as you do in chainsaw tests, because a lot of chainsaw tests are kind of like… I created X, and now Y should exist, eventually, right? Whereas these tests are more like… Israel.
these tests are more like, I create a bunch of stuff, then I wait for, like, this one deployment that I care about to be ready.
And then I start asserting at the, like, I start hitting the HTTP server somewhere and asserting things about the data that it gives me.
My tests… those tests also have, like, a… make a small… binary, which is essentially just, like, an OTLP receiver plus a relay?
Where I thought about all sorts of… Alternatives to it, and landed on it, because it was simple enough, and there's, like, not… There's not… there doesn't exist a backend for telemetry that you can easily query from outside the cluster, essentially.
**Jacob Aronoff** 39:16 Hmm.
**Mikołaj Świątek** 39:17 That is, like, perfectly native.
**Jacob Aronoff** 39:20 Because… Becoming hotter of, like, we could just dump S3 to, like, an in-cluster MinIO, and then query that with DuckDB.
**Mikołaj Świątek** 39:29 I think that's more complicated than what I have.
I have… I have checked that. What I have is, like, a single… single application that is… just receives the data and just stores it in memory, and you can hit an endpoint, and it gives you back the data also in auto-format directly. So…
**Jacob Aronoff** 39:48 So it's just like a… like a mirror.
**Mikołaj Świątek** 39:51 Yes, that's all it does.
And that's enough for all the tests that I've written.
**Jacob Aronoff** 39:57 Yeah, yeah.
I mean, mostly that's what we care about, right? But, like, shape N is the same shape, or the expected shape is what we want it to be.
**Mikołaj Świątek** 40:06 Yeah, so I'm saying all of this as just, like, a PSA, because I don't really need anyone to do anything right now about this, I'm just saying that there's going to be pull requests implementing tests this way, so you guys are aware.
**Jacob Aronoff** 40:20 Yo.
**Mikołaj Świątek** 40:20 That's what's happening.
Next in line is feature gate stability, and the… Pavol, there's, like, two feature gates that you added, which are about, like, operand network policy and Operator Network Policy, they're both in alpha.
Do you… are they gonna go to beta?
Are there plans?
**Pavol Loffay (Red Hat LLC)** 40:50 Yes, so the network policy, yes. What is the other one?
**Mikołaj Świątek** 40:54 There's two, there's network policy, there's operator.network policy, and operand.network policy.
**Pavol Loffay (Red Hat LLC)** 41:02 Yes.
**Mikołaj Świątek** 41:02 One is for the Operator, one is for the collector.
**Pavol Loffay (Red Hat LLC)** 41:06 Yeah, it has been enabled on OpenShift for a couple of releases, and I think it works well, so I'm… Confidence to enable it by default.
**Mikołaj Świątek** 41:16 Okay. That case can create issues for them, where we track the… life cycle.
This doesn't fully help, because… but it helps a little bit.
**Pavol Loffay (Red Hat LLC)** 41:29 Sorry, what did you say? I was… I was looking at you.
**Mikołaj Świątek** 41:32 Just to create an issue for… to track the lifecycle of them. Okay. So we're, like, we eventually delete them.
After getting them to stable.
There's also, like, an Operator Collector used default telemetry shape, which is something a contributor added, and then they promised they would take care of it, and they didn't, so I might take care of it myself. It's… but that one's in beta, so it's just a question of getting it stable eventually.
And finally, finally, there is… Operator Golang flags, which is what sets GoMEM limit and go maxbox.
**Jacob Aronoff** 42:18 That one we could probably do, that one's been there for a while.
**Mikołaj Świątek** 42:21 Yeah, and we should, and we talked about this, I think, multiple times, and it hasn't happened. I think it's a sign to Bene, who isn't here, conveniently.
I have no idea what a good way of tracking these flags is. I thought of, like, multiple approaches, and all of those are, like, in some way more painful than the situation that we're in.
Like, I thought about, like, failing CI if there's some, like, time period after, like, you add a… you add metadata to each flag, and if it's indicating where it should be flipped, and if it's not flipped by that time, CI starts failing completely. But I don't think that's a good idea, because there should be, like, one person responsible for it, and it shouldn't be, like, everyone else's problem, right?
But if you don't do it this way, how do you ensure that it actually happens?
**Jacob Aronoff** 43:14 I don't know. It's organization, and organization is hard.
**Mikołaj Świątek** 43:22 It's not a big problem, we don't have that many feature gates.
**Jacob Aronoff** 43:25 Meeting.
**Mikołaj Świątek** 43:27 The, the one for… What's it called? Target allocator fallback strategy is gonna go away soon, because it's just going to become an option. I already have, like, a pull request for it, I just haven't, like… Completely made my peace with the implementation decisions.
inside it.
And that's it.
And issues to discuss at SIG.
Actually, let me share my screen, because this is… There's some interesting stuff here.
**Jacob Aronoff** 44:01 O?
**Mikołaj Świątek** 44:04 Where is my window?
This way…
**Jacob Aronoff** 44:10 Yeah, the OTLP self-Telemetry.
**Mikołaj Świątek** 44:14 Yeah, and I think this pull request is fine.
Can you see my screen?
**Jacob Aronoff** 44:21 Yes.
**Mikołaj Świątek** 44:24 Right, so this is… this has already landed in Target Allocator, in the configuration.
And it currently does not use the creative config, but it uses… It uses a subset of the creative config, intentionally, so we can switch to the creative config later without breaking anything.
And the same principle is applied here.
Like, this pull request is actually, despite it being plus 2,000 lines, is actually really simple, because it's really just that it's a bunch of types, and then, like, serializes those types to put them in the target allocator configuration, and that's it.
That's all that happens.
I'm mostly bringing it up here because I feel like, Pavol, you've… you've… kind of… Gone through the exercise of, of, like, having… declarative config inside the CRD.
I wanted to have your opinion.
**Pavol Loffay (Red Hat LLC)** 45:24 Yes, it's been some time since I looked at it.
So what exactly would you like to know?
**Mikołaj Świątek** 45:33 Basically what…
**Pavol Loffay (Red Hat LLC)** 45:34 Certilize.
**Mikołaj Świątek** 45:36 I eventually would like to embed the collaborative config here.
Or something like that.
And I'm wondering how to do it.
**Jacob Aronoff** 45:52 I think…
**Pavol Loffay (Red Hat LLC)** 45:52 narrative constig?
**Mikołaj Świątek** 45:55 Or something like it.
Maybe, maybe this can just be an unpyped map that we say this is the clarity of config, but… Yeah, basically, I want the target allocator configuration, it's kind of normal configuration that you put in there to accept the declarative config, to configure telemetry in a very similar way to how The collector does it.
that's one thing I wanna… I wanna do eventually. And the other thing is that the CRD should also allow configuring this however you want.
Basically, I want to standardize.
And, and, like, not… not worry about it anymore.
**Pavol Loffay (Red Hat LLC)** 46:43 I think if we… we should use the same structure in the instrumentation and gear.
What are the problems?
**Mikołaj Świątek** 46:53 I agree. I agree.
**Pavol Loffay (Red Hat LLC)** 46:54 If we need the full declarative config in the Georgetown Creature, which I don'.
**Mikołaj Świątek** 47:00 I don't know… I don't know if we need the full thing.
Maybe we need a subset of it, but if we want this to be a subset of it, then we need to have some way of Verifying statically that it's actually a subset of it, right?
**Pavol Loffay (Red Hat LLC)** 47:15 Good.
**Mikołaj Świątek** 47:16 And I think the way that that should have to work is that You take the struct that's here.
you serialize it into JSON or YAML, and then you try to load that JSON or YAML into the declarative config parser.
And see if that succeeds.
I think that's how it would have to work.
Does that make sense?
**Pavol Loffay (Red Hat LLC)** 47:44 Yes, I think… maybe what I would… prefer is to have the proper fields defined in the CRD for the declarative config, so… it shows up properly on the CRB.
I know that there are some fields that are not stable yet, which make it more complicated.
But if there are… if there is a combination of stable and unstable fuels, maybe we can deal with it on the CRB as well, in a proper way.
**Mikołaj Świątek** 48:23 I think… I think we just shouldn't have unstable fields, honestly.
like, this is… this is a different case than the instrumentation, because here you're just configuring telemetry for, like, a Go application directly. So you might not need all of it. But it should be… like, my requirement, like, we don't have to put all the fields in here, or we don't have to put all the fields right now.
But we should be able to in the future. Like, we should not… what we should have here should not contradict the creative conflict.
Is my requirement for it.
And I'm wondering how to ensure that is true.
**Pavol Loffay (Red Hat LLC)** 49:09 We need to go through the exercise of trying to put the decorative copy into CRT and see how it works.
**Mikołaj Świątek** 49:16 You're right.
**Pavol Loffay (Red Hat LLC)** 49:16 I don't that.
It was a long time ago, I don't remember. I don't think it was fully functional.
I don't even remember how I dealt with the unstable yields.
**Mikołaj Świątek** 49:33 I think the only way to deal with them is to just not have them.
I can't think of any other way.
Anyway, we don't have to… we don't have to, like, decide about this. I think this pull request is largely okay. I just want to… I'll get the offer to verify for… because I think this is largely correct, like, this pull request is mostly just, like, bureaucracy.
It doesn't do much interesting. The main interesting thing about this is the actual shape of this configuration, and again, I want to just add a test that verifies that it's compatible, and I am okay merging it as is, and we can think about… How we.
**Jacob Aronoff** 50:17 The only thing…
**Mikołaj Świątek** 50:17 evolve it later.
**Jacob Aronoff** 50:19 Yeah, the only thing that I would change is maybe not call it, Target Allocator Telemetry Config, and just call it, like.
Experimental declarative config or something?
**Mikołaj Świątek** 50:31 But it's not experimental.
**Jacob Aronoff** 50:33 Well, for us, it is.
**Mikołaj Świątek** 50:35 No, it's nuts.
**Jacob Aronoff** 50:36 We don't have it right now.
**Mikołaj Świątek** 50:38 We do.
**Jacob Aronoff** 50:40 Where's declarative config?
We don't give you credit for that.
**Mikołaj Świątek** 50:43 Correct.
We don't have the clarity config, but we have a subset of the clarity config.
used in the target allocator application that is used to configure it. In particular, you can make it output metrics via OTLP.
And there's been a test in this pull request that verifies this.
**Jacob Aronoff** 51:04 Yeah, I think.
**Mikołaj Świątek** 51:04 Bless you.
**Jacob Aronoff** 51:05 I'm just saying that we could probably make the name of this object, this struct, more generic than target allocator telemetry.
Given that there's nothing Target Operator specific in there.
**Mikołaj Świątek** 51:19 Is Target Allocator specific in that it contains exactly the fields that target allocator accepts right now?
**Jacob Aronoff** 51:27 Okay, I guess that's fair. I guess in the future.
**Mikołaj Świątek** 51:31 We can rename it. If there's, like, more instances of it elsewhere, then we can rename it. It doesn't matter for the CRDs anyway, because they are gonna have a copy everywhere, it appears, so…
**Jacob Aronoff** 51:43 Yeah, and it is just called telemetry. The tag is not target allocator telemetry.
**Pavol Loffay (Red Hat LLC)** 51:48 We'll be able to refactor it afterwards, once we have the genetic one.
**Mikołaj Świątek** 51:53 As long as it's compatible, as long as it's backwards compatible, then yes, we can… or forward compatible, I suppose, in this case. It's okay. All right, so cool. That's what I thought, and it sounds like we agree. You can review this if you want, but you don't have to.
And the other thing we had was… Give me a sec.
Let's talk about Ruby.
This is FYI.
There's a conversation happening to hear about, like, what is necessary for the Ruby auto instrumentation.
We don't have to talk about it right now, but you should take a look, as it affects what we're going to maintain in the future. I am… my position in here is that the… my line is drawn at the way Java and .NET work right now, for us, by which I mean… The way we build images for Java and .NET is that we just download an artifact from upstream, we put it in the image.
Done.
In .NET, we also, like, we do a bunch of, like, sim links, because there's, like, the muzzle version and blah blah blah, but, like, we don't build anything on any of those.
I am against accepting any proposal that requires us to maintain this image and maintain its list of packages.
I don't want a second Python auto-instrumentation where there's, like, a list of packages there, and if somebody comes in and asks me why this and not that, I don't have any answer to that question.
It is a historical artifact.
So that's… that's… that's my opinion. If you have a different opinion, let's talk in here.
Yo.
**Jacob Aronoff** 53:55 Let's take a look at that.
**Mikołaj Świątek** 53:56 Yeah, Ruby now is support… is supported by the auto-injector, so that should make things… simple, conceptually. It's gonna be the first… if it goes in, it's gonna be the first instrumentation to just use the injector always.
throughout.
**Jacob Aronoff** 54:11 It'd be great. It'd be good to also have that as, like, the sample case, and then we could develop a bunch of, like, net new tests around it as well.
**Mikołaj Świątek** 54:18 You know?
Yeah, so that's it. Do you guys have anything you want to talk about? Start on the list?
**Jacob Aronoff** 54:28 No, my brain is mush.
**Mikołaj Świątek** 54:37 Right.
In that case… the… somebody has to make the issue for the new security advisor.
**Jacob Aronoff** 54:47 Oh, that's… that was the thing. Yeah, I can do that.
**Mikołaj Świątek** 54:50 Okay, you can do that, and I'm gonna take care of the one that we still have open, where I have to go and, like, bother someone from admin for a bunch to make it work out the way I want.
But at this point, we have, like…
**Jacob Aronoff** 55:05 Bug Jirassi, because I think that he's our, like, liaison or whatever, and the… That channel that we have with him.
**Mikołaj Świątek** 55:13 Yeah, but, like, he linked me to the right, to the, to, like, a documentation under community, which… Specifically outlines how to do this.
And who's responsible, because the, there's, like, an on-call rotation for this among GC members.
You have the permissions to do it.
And I basically… it's on my list. I have to go talk… find… find whoever's on call and just ask them to, like… reopen a previous advisory, they move one person to the other, so he's the original reporter, and then close it with a CVE number assigned.
And then in the original one, close it with a documentation issue.
That's how it has to happen, but I haven't done that yet. But I will. I will definitely do it by the end of next week.
**Jacob Aronoff** 56:11 Cool. Yeah, and I'll just… For the other one, I can open up… I'll just, like, make the docs change, and then we can just close it.
**Mikołaj Świątek** 56:20 Yeah, now that we have docs reorganized, it's much easier to make these changes.
**Jacob Aronoff** 56:24 Yeah, yeah.
**Mikołaj Świątek** 56:26 By the way, am I the only person who got kind of pissed off by that report?
**Jacob Aronoff** 56:31 I think it's really dumb. I think that this is, like… really silly. I think that there's a bunch of people who just, like.
Throw an agent at, like, repos now, and they're just like, give me, you know, Find me security bug.
**Mikołaj Świątek** 56:45 But it's like, the worst thing is that it's, like, so… why is it so much text if the only thing you're saying is that the default is insecure? That's correct, but it's correct intentionally, right? Okay, you can have a… you can have, like, a discussion about whether it's correct to have this default, right?
We have reasons to have it, but, like, why is it, like, several paragraphs of text describing some, like, POC whatever crap about it? Like, it's… it was already in the original… the original report.
And I, honestly, I get that kind of stuff. Maybe I shouldn't say it when it's recorded, and I have, like, there's an irrational, irrational, desire in me to deny the reporter credit for it.
**Jacob Aronoff** 57:35 This was, like, the one that I got a few months ago that I… that I was like, this is just not an issue, this is just how Kubernetes works, and people are just silly, you know? It's… it's just the nature of it, unfortunately.
**Mikołaj Świątek** 57:47 Yeah. Well, we are… we aren't getting that many, at least.
Yeah.
**Jacob Aronoff** 57:52 We're not. Other people are.
**Mikołaj Świątek** 57:56 Okay, it was good to talk to you guys.
**Jacob Aronoff** 58:00 assume.
**Mikołaj Świątek** 58:01 time.
**Jacob Aronoff** 58:02 Yeah.
**Pavol Loffay (Red Hat LLC)** 58:02 Goodbye.
