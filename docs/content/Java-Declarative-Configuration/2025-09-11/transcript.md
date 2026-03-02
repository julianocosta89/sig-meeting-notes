SIG: Java Declarative Configuration
Date: 2025-09-11
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:24 Hey, Gregor!
**GZ Gregor Zeitlinger** 00:27 Hello, Trask.
**Trask Stalnaker** 00:30 How's it going?
**GZ Gregor Zeitlinger** 00:34 Good.
**Trask Stalnaker** 00:39 What's that statue, bust in the… background.
**GZ Gregor Zeitlinger** 00:46 That's, something my son did at school.
**Trask Stalnaker** 00:51 Oh, that's amazing!
**GZ Gregor Zeitlinger** 00:58 Also, the other things, but you can hardly see them.
Hi, Jay!
**Jay DeLuca** 01:09 Hey, guys.
How's it going?
**Trask Stalnaker** 01:13 Good, good…
**GZ Gregor Zeitlinger** 01:15 Good.
Hi, Robert.
**Robert Niedziela** 01:24 Hello.
**Trask Stalnaker** 01:26 Ayy.
Next declarative config meeting… okay, thank you. Anonymous hamster.
Alright, yeah.
So, let's… Focus on… PRs for the release. Alright, so… Got…
Plenty of approvals on this. Let me just check…
Remind myself what we did here…
**GZ Gregor Zeitlinger** 02:34 We talked about it last week, and, Jay had a…
Suggestion on the name, that profile could be confusing, because profile is also a signal.
**Trask Stalnaker** 02:48 Right.
**GZ Gregor Zeitlinger** 02:51 And, so it's instrumentation mode.
**Jay DeLuca** 02:56 We might have forgotten to update those.
Yeah.
**Trask Stalnaker** 03:01 And so the file format… oh yeah, yeah, so maybe just, everywhere.
**GZ Gregor Zeitlinger** 03:13 Yep, right.
**Trask Stalnaker** 03:14 So, instrumentation, profile, I see, so…
CSV source… Oh, this is so confusing. Okay, I get it, I get it.
**GZ Gregor Zeitlinger** 03:38 If you have a different preference, I'm happy to change.
**Trask Stalnaker** 03:42 It's fine.
So, instrument to a Java agent, and then…
It might… if it… it's a little hard to…
follow… but probably part of that is spotless. I see the indentation there, yes. Okay.
I've been using Python a bunch lately, and they have very nice string templating stuff that makes this.
cleaner.
Okay. Yeah.
That looks great. I would… from a testing…
I'd love to… we'll merge this as is, but let's…
talk, like, the… I really like the smoke test.
That you added.
And would love to expand more on that, because, like, one of the ways that
I can understand the declarative config stuff better, is to look at the tests and look at the YAMLs that…
It's testing
Alright.
**GZ Gregor Zeitlinger** 05:09 Will you want to have this rename as a follow-up, then?
**Trask Stalnaker** 05:12 Oh, oops. Sure, yeah, yeah, do it, yeah. This variable renames, yes, yes, thank you.
**GZ Gregor Zeitlinger** 05:19 And the smoke test.
**Trask Stalnaker** 05:22 The smoke test… yeah, well, the smoke test was in a different…
Oh, did you merge… did we merge… did we get the smoke test merged already?
**GZ Gregor Zeitlinger** 05:32 No, but I mean… I can do the same pattern.
**Trask Stalnaker** 05:39 Oh, I see, for a separate smoke test for that.
Yeah, I guess…
**GZ Gregor Zeitlinger** 05:44 later. It's… it's the other PR that we're, covering next, the resource providers, has it?
**Trask Stalnaker** 05:51 Okay.
Yeah.
**GZ Gregor Zeitlinger** 05:54 just didn't manage to get it into Java, because there's some infrastructure in the groovy tests that work differently.
So I gave up on doing that in Java.
**Trask Stalnaker** 06:06 I, I… Thought that might… Be the case.
Okay… So, over here… okay, yes, this has the tests, yes, I was starting to look at that.
And it has… yes, I love this.
I can see exactly what's happening.
So yeah, so as far as… adding more… Declarative config smoke tests?
Two options. I think either one is fine of whether combining more Into a single test.
Kind of like a kitchen sinky thing.
Or the other is to split them out in separate tests, I think either.
is fine.
**GZ Gregor Zeitlinger** 07:05 Okay, yeah, I'll think about what makes more sense.
**Trask Stalnaker** 07:09 So… okay, so we've got this, we've got our resource attributes.
And we're verifying…
Yes… Service… detector… Right.
Do we produce this by default? Service instance ID?
**GZ Gregor Zeitlinger** 07:40 We do.
**Trask Stalnaker** 07:41 Okay.
Cool.
I just know it's not stable yet, but that's okay. I mean, we produce lots of telemetry that's not stable.
Yeah.
**GZ Gregor Zeitlinger** 07:51 Getting that to stable is another project.
**Trask Stalnaker** 07:55 Another project which we are actually kicking off.
**GZ Gregor Zeitlinger** 08:00 That's good.
**Trask Stalnaker** 08:01 Yeah.
Distro Detect… Dear… okay. Yes.
Okay, so what about,
all of… these other… Detectors… Can we add…
Can we add verification? I mean, I guess, obviously, not for, like, a Kubernet… Do we have a… not for, like, a container one, we probably won't get anything. Maybe. We're running in…
But, like, host…
**GZ Gregor Zeitlinger** 08:49 Are you asking if we have pests for them?
**Trask Stalnaker** 08:51 Yes, specifically for declarative config, like, should we add… should… can we… assert more resource.
attributes over here.
**GZ Gregor Zeitlinger** 09:09 Could add more, yeah, we could add more to this test.
**Robert Niedziela** 09:16 For resource detectors, it may be sometimes tricky, right? Because they may require a specific environment to run. A lot of mocking may be required, or something like that.
**GZ Gregor Zeitlinger** 09:28 I mean, we already have this with the existing tests, so we… I mean, we would throw more tests into the single test.
I'm wondering what additional, Confidence we would gain.
**Trask Stalnaker** 09:45 That they are getting picked up.
in… declarative config…
**GZ Gregor Zeitlinger** 09:56 Right, so you don't want to test, like, for the specific host name, just to make sure that they are getting picked up.
**Trask Stalnaker** 10:06 Yeah, yeah, I just want to, the… For me, the smoke tests… Give me the…
Overall, okay, this is… it's all packaged up, and it's all working together with declarative config.
**GZ Gregor Zeitlinger** 10:25 Okay.
**Trask Stalnaker** 10:26 But I agree, I wouldn't go so far as, like Robert says, with the, you know, if it requires weird mocking stuff, like the container ones.
If it's not easy, don't… don't worry about it, but if it's, like, host.
You know, it's probably easy to just add An extra assertion over here.
**GZ Gregor Zeitlinger** 10:48 Okay.
**Robert Niedziela** 10:51 Yeah, and the side question, do we have some,
let's say, convention for naming of resource providers. I mean, sometimes we talk about detectors, sometimes it's… it's called component provider, resource provider.
I think it would be good to establish some convention here.
**Trask Stalnaker** 11:16 the spec… I believe the spec calls them detectors.
**Robert Niedziela** 11:20 Hmm?
**Trask Stalnaker** 11:21 And so that's the terminology that we should use in, I think, user-facing?
Stuff, if possible.
The complication is that the SPI is called Resource Provider.
And so, like, internal stuff is gonna be called resource provider, but that's, I think, where I would draw the line, if… if we can.
**Robert Niedziela** 11:56 We could do some cleanup, right?
rename them to Common Convention at some point, at least.
**Trask Stalnaker** 12:06 Yeah, I think the best chance we have at that will be when entity entities…
Gets prototyped and stabilized.
Yes, hopefully we can correct.
That going forward.
I'm not sure if… we'll be… I'm not sure if we'll get buy-in on… Changing the existing… stable.
**Robert Niedziela** 12:35 Okay.
**Trask Stalnaker** 12:35 resource provider, especially because, I mean, John…
There is an argument for calling it a provider, because it is a SPI in Java terms, it is a service provider.
**Robert Niedziela** 12:49 I believe we have arguments for all naming conventions we use in.
**Trask Stalnaker** 12:54 Oh, yeah, for sure.
Let's see, what else? Jar, maybe… No, JAR service… Go ahead.
So we won't have jar service name extractor, because we are… Picking that up.
We're explicitly declaring that.
Manifest. What do we do? Oh, that's another serv… just service name, so maybe process… resource…
Okay, so maybe those are the only two additional ones that are…
Easy.
**GZ Gregor Zeitlinger** 13:44 I've put in the name of an existing declarative configuration test, which is a unit test, but it also shows how it is used.
Just as a different… type of test.
Right, there you also see the YAML.
**Trask Stalnaker** 14:13 Oh yeah, yeah, that's nice, yes.
And, oh, that's a good point. So do… is this… oh, this is library.
Can we run this test in the Java agent, also?
**GZ Gregor Zeitlinger** 14:36 You mean in the smoke test, or, somewhere else?
**Trask Stalnaker** 14:39 No, I mean in, Oh yes, I think we discussed this last time.
the Java… there's no Java agent package here.
**GZ Gregor Zeitlinger** 14:50 Right.
**Trask Stalnaker** 14:51 So… Maybe, like, a…
even though it's not a convention, because we looked, I thought it was, but, like, a Java agent dash testing.
module here.
Something that was just to… Test, run this same test.
under the Java agent, as well.
**GZ Gregor Zeitlinger** 15:20 This doesn't do anything different. It uses the same… because it is loaded by the SDK directly.
So, it's, it's a weird,
Between… in between, between, testing just the library and testing the smoke test.
**Trask Stalnaker** 15:41 So, can say that again?
**GZ Gregor Zeitlinger** 15:47 It's a middle ground between the library test that we already have and the smoke test, and I don't see.
**Trask Stalnaker** 15:53 I wanted to…
**GZ Gregor Zeitlinger** 15:54 Right, in addition to this test.
**Trask Stalnaker** 15:57 Right, okay, so we had discussed… okay, that's why we went to the smoke test, yes. That makes sense to me.
So… Yeah… So it looks like we could basically do these same, potentially.
Let's see if that link actually works.
Yeah… Kind of.
What is?
Is this actually Column? Yeah, oh wow, look at that.
Hadn't seen that.
Through 78, I don't…
Yeah, that's the link I want.
Yes, makes sense, Carter. Yeah, we'll, we don't need that intermediate test, yes, we'll just do the smoke test for that same behavior. Cool.
What else do we have here? So…
Incubator, because that's where declarative Config lives today.
Jar service name…
**GZ Gregor Zeitlinger** 17:51 Yeah, this is another name that I came up with, Robert, since you mentioned it. It's,
The… so… so to speak, the business logic, of the… resource providers.
**Trask Stalnaker** 18:08 Oh, and that's because to allow it to be used from the declarative config one also.
**GZ Gregor Zeitlinger** 18:13 Right.
And in my previous attempt, I had mixed this up, and from your comments, Trask, I reasoned that this is confusing, so I split this up.
**Trask Stalnaker** 18:25 Okay.
later… Manifest resource extractor, okay, got it. And jar, service name… resource.
actor.
Nice. Yeah, yeah, yeah.
Process arguments, okay…
Nice.
Yeah, I'm hoping, once Jack is back, and hopefully he'll agree with, removing the generic type off of component provider.
I don't know if you saw my PR to the core repo.
**GZ Gregor Zeitlinger** 19:19 Yeah, I already commented on that, but I'm not going to.
**Trask Stalnaker** 19:22 You won't need…
**GZ Gregor Zeitlinger** 19:23 Get us sidetracked.
**Trask Stalnaker** 19:25 Oh, yeah, yeah, no, no.
Sorry.
**Robert Niedziela** 19:30 Do we have an idea when Jack is back? Not really.
**Trask Stalnaker** 19:33 He just started checking in on Slack, so… I think he's…
But I don't know when he's back full.
**Robert Niedziela** 19:46 Okay.
**GZ Gregor Zeitlinger** 19:46 He, told me that he's planning for 6 to 8 hours for a week.
So, we probably cannot expect in-depth PR reviews in the near future.
**Trask Stalnaker** 20:07 Manifest, okay, this is the extracted logic… Suspect units…
Okay, and the tests…
Resource… Yay… What, can you just briefly…
If you remember what the change here was…
**GZ Gregor Zeitlinger** 20:47 So…
The extractor is doing the actual logic, and so there is an extractor test for manifests that is actually
doing the reading, and this part is just the scaffolding around it, and therefore, it's not actually using open class paths. But if you go to the manifest extractor test, then you can see that
It still has this ClassPass reading.
**Trask Stalnaker** 21:19 What are the two… I guess the part that I was a little not following, what are the two different resources?
Here, being passed in, and maybe I just need to scroll down…
**GZ Gregor Zeitlinger** 21:35 It's service, name and version.
**Trask Stalnaker** 21:38 Oh, was this Open ClassPath resource returning a,
No, it was an input stream.
**GZ Gregor Zeitlinger** 21:47 It was returning input stream, but the input stream reading is extracted to the extractor.
**Trask Stalnaker** 22:01 I see, resource… I was just trying to understand the resource input…
**GZ Gregor Zeitlinger** 22:10 But in the end.
**Trask Stalnaker** 22:11 Oh… oh, I see. Gotcha. Yes, yes, I understand now. So this is… you're skipping that part now, because that part is now tested.
In the extractor.
**GZ Gregor Zeitlinger** 22:28 Right.
**Trask Stalnaker** 22:29 Cool.
Jar service name… Resource… okay, and that…
this resource extract… okay, so that's, yes, the opening ClassPath resource.
What happened here?
If you remember.
**GZ Gregor Zeitlinger** 22:56 Yeah, this is, caused by the addition of the… Incubator.
And the dependencies.
And the incubator is also, triggering, this view config.
To be interpreted, and then it says, oh, this is not a valid file.
**Trask Stalnaker** 23:17 Oh, I see, this is the properties we're feeding in, this is the
I see, we're not asserting against this, this is just.
**GZ Gregor Zeitlinger** 23:29 Yeah, in that case, we're just testing that it can be converted into a list, because Spring needs special assistance with lists.
**Trask Stalnaker** 23:41 Okay, makes sense. Thank you.
Okay…
Component provider…
Just… Component provider…
Oh, I see. In these cases, you don't need the… there's no read point in the extractor, because it can just… there's no configuration.
So it's just a.
**GZ Gregor Zeitlinger** 24:30 static.
**Trask Stalnaker** 24:33 Makes sense.
Art detectors…
Okay, this part looks interesting…
Resource Customizer… Provider… So this is the part where we are…
Providing… we're adding our own defaults.
**GZ Gregor Zeitlinger** 25:13 Yep, because we want to avoid that,
Users go without this, and then… And not, troubleshoot.
**Trask Stalnaker** 25:24 Right.
And so… We're saying, hey, we're always going to add.
**GZ Gregor Zeitlinger** 25:37 Great.
**Trask Stalnaker** 25:41 I'm just trying to think if that's what we want or not.
Always, like, Because it's out of sync with the SDK…
**GZ Gregor Zeitlinger** 25:56 Sorry, what is the SDK? What do you mean by with the SDK?
**Trask Stalnaker** 26:01 Well, I guess, I mean, just the general declarative config, where you have… you're… you have to opt in to all the resource detectors.
**GZ Gregor Zeitlinger** 26:13 Yeah, right, already discussed this with, Jack, Couple months ago.
But from the SDK point of view, there's nothing there. But, it's up to every distribution, including the Java agent, to decide if they want to have something that's always there.
**Trask Stalnaker** 26:38 Right.
And I guess, so my question is, do we… Wanted to always be there.
**GZ Gregor Zeitlinger** 26:52 So,
I think yes, because the distribution is similar to the telemetry language and SDK. It allows you to find out
what a library version you were… what… oh, not library, what version of the agent you were using to report a bug. So it's basically making our life easier when we get bug reports.
**Trask Stalnaker** 27:21 Yeah.
Yeah, I agree. I think I definitely agree on distribution.
What about service?
Service Resource Detector.
**GZ Gregor Zeitlinger** 27:37 Yeah, service is, the, primary…
identifier for a service. For that reason, service name is already required.
But if you don't add the detector, then you will just have unknown Java, and that is just a fallback.
And… Therefore, every user would have to add a service to get a meaningful service name.
**Trask Stalnaker** 28:07 What about hosts, these other resource detectors? These ones, users would have to opt into? Like, the…
Jar, service, name… host resource… I see, so this one is… Only…
the environment variable? You know, which…
**GZ Gregor Zeitlinger** 28:34 You mean what service does? You cannot see it in the code here, because the detector is actually implemented in the SDK.
**Trask Stalnaker** 28:44 Yeah, there's a comment there.
**GZ Gregor Zeitlinger** 28:46 Where it is.
**Trask Stalnaker** 28:48 Aw, thanks.
**GZ Gregor Zeitlinger** 28:50 It's adding the service name and service instance ID.
Yeah, it's also there in the comment.
**Trask Stalnaker** 28:58 Perfect, okay.
So this is… Service, resource, detector.
And how does this… Interrupt if somebody also adds…
Like, the jar resor… jar service name?
detector… Into the declarative config.
Will… do we know which one will take precedence in that case?
**GZ Gregor Zeitlinger** 29:38 Yes.
the user just has to specify the precedence, so if they want to have service first, then they add service and jar. If they want to have it the other way around, they just do it the other way around. If they miss to add service, then we just add service at the end.
**Trask Stalnaker** 30:00 Does the end get precedent, or does the beginning get precedent?
**GZ Gregor Zeitlinger** 30:08 I have to look it up, I don't remember.
**Robert Niedziela** 30:13 I think it may also depend on… on the… Hmm…
Detect… no, detector, no, because detector is always creating a new resource, and they are merged one by one, so…
I think the last one wins.
**GZ Gregor Zeitlinger** 30:28 I also think so, but I'm… I'm going to double check.
**Trask Stalnaker** 30:35 Okay, let's, so, should we add the… our detectors first?
So that the users can override them.
**GZ Gregor Zeitlinger** 30:49 They are only added if not there, so if, we are not changing it if the user already has it somewhere. That's why you have the if at line 55.
**Trask Stalnaker** 31:00 Right, but what if they add another service detector, like the jar service name detector, something else that…
Populates a more specific service name.
**GZ Gregor Zeitlinger** 31:17 You mean we should add ours so that it will have the least precedence?
**Trask Stalnaker** 31:23 Yeah…
**GZ Gregor Zeitlinger** 31:25 Yep.
That's a good idea.
**Trask Stalnaker** 31:39 Okay, service, yeah, so service… What does… I forget, service… Hands…
So we get service instance ID…
And I have the environment variable name.
**GZ Gregor Zeitlinger** 32:04 Right.
**Trask Stalnaker** 32:09 Do we want…
**GZ Gregor Zeitlinger** 32:10 Oh, good one?
That one should actually have the highest priority for service.
**Trask Stalnaker** 32:19 Oh, is… yeah, what does this mean in… declarative config terms…
Is this only going to be environment variable and system properties?
**GZ Gregor Zeitlinger** 32:35 This is… Build the environment variable, because it uses the default config properties.
**Trask Stalnaker** 32:48 It's like…
**GZ Gregor Zeitlinger** 32:49 An exception, because usually you don't have it.
**Trask Stalnaker** 32:54 So that's kind of, though, a little bit…
Out of sync with the declarative config message that it doesn't support.
environment variables…
**GZ Gregor Zeitlinger** 33:12 That is true, and I think it was discussed,
But, it's too long ago to give you the exact reasoning.
**Robert Niedziela** 33:24 Yeah, resource detectors are really special kind of component providers. They are treated in a different way.
**GZ Gregor Zeitlinger** 33:31 Right, but Trask was just referring to why are we reading environment variables At… only at that place.
**Robert Niedziela** 33:39 Okay.
**Trask Stalnaker** 33:42 Do we… Let's see what…
**Jay DeLuca** 33:46 We do have at least one other environment variable, right, for the debug logging?
**GZ Gregor Zeitlinger** 33:55 But this is an agent. We were just, looking at SDK land.
**Trask Stalnaker** 34:05 Because I… I feel like with declarative config, we're…
We're telling people to do this.
If they want, instead of using the… Environment variable.
Well, we probably have a migrate… I think we have the migration config.
Which… People can use if they still want to do that.
But overall, we're… Trying to move to this is the preferred.
**GZ Gregor Zeitlinger** 34:53 Yep, that's true.
Well, I would still, not agree, because it has,
service instance ID, and I also think there was a good reason why we had
While we are reading environment… the environment variable there, I just have to check what it was.
**Trask Stalnaker** 35:21 Okay, yeah, I'll leave the comment that, yeah, you can… Look for history there.
I think distribution is a very easily defendable
One to put in, because it is our distribution.
That were, publishing, like, so it feels… like, not a…
It's something unique to our distribution.
I don't know. I feel like that one's easier for me to defend adding it by default.
Okay, let's see, anything… oh, how would somebody remove if they didn't want our distribution?
resource detector? How would they remove it?
**GZ Gregor Zeitlinger** 36:37 I think the only way is to add it to the exclude list.
**Trask Stalnaker** 36:43 Oh, that would work. There's an exclam.
**GZ Gregor Zeitlinger** 36:45 That would still work But I would not recommend doing that.
**Trask Stalnaker** 36:50 Resource…
Where is… do you know if… is that part of the…
**GZ Gregor Zeitlinger** 37:02 Is this…
**Trask Stalnaker** 37:02 declarative config.
**GZ Gregor Zeitlinger** 37:04 It is… should be there.
**Trask Stalnaker** 37:07 Source attributes…
**GZ Gregor Zeitlinger** 37:14 I'm also looking…
**Trask Stalnaker** 37:15 Okay, so… oh, I see here, yes, yes, I understand. So…
**GZ Gregor Zeitlinger** 37:23 Right.
**Trask Stalnaker** 37:27 Distrib… okay, so we need a name, so what is our name of our… Distro… Shhh.
I wonder if we should have… I wonder if our distro name should be… Something more unique, like…
So that people could…
disabled…
**GZ Gregor Zeitlinger** 38:06 That's… that's, pretty much how it is. I think hotel…
Java instrumentation or something like that.
You can see it in the chest.
**Trask Stalnaker** 38:18 Oh, no, but the name of it, meaning how would people… what name would people put here to exclude it?
**GZ Gregor Zeitlinger** 38:26 It's the name of the attributes, not of the detector.
**Trask Stalnaker** 38:30 Oh, it is?
**GZ Gregor Zeitlinger** 38:32 Yep.
**Trask Stalnaker** 38:37 include, attributes. Oh, okay.
Resource detectors… Applies after…
Okay, where are… oh, here's the detectors, got it, okay.
So, this name here… ICM, because this name is… include only…
And this is where you're adding to… you're adding it here.
**GZ Gregor Zeitlinger** 39:11 Huh.
**Trask Stalnaker** 39:15 I still wonder if we should have a…
If our… the name of our distribution detector should be specific to us.
Right, because there could be multiple distribution detectors.
out in the world.
So as opposed to… this one is container detector, right? It's generic, or container semcon.
our distro detector isn't generic.
It's specific to our Java agent.
**GZ Gregor Zeitlinger** 39:57 Yep, that's true.
**Trask Stalnaker** 39:59 So if… if Grafana had a… distro of the Java agent.
You would have a different detector?
Distribution detector?
**Robert Niedziela** 40:15 That's actually my case, I implemented my own destroy detector in Splunk.
**GZ Gregor Zeitlinger** 40:22 And you give it a different name?
**Robert Niedziela** 40:25 Oh, I call it, I re… let me check.
**Trask Stalnaker** 40:36 But if you give it… Gregor, if you give it the same name.
Won't it conflict? Like, when we look up the SPI?
**Robert Niedziela** 40:44 enlighten.
**GZ Gregor Zeitlinger** 40:48 That is true, that is something to figure out, yeah.
I wonder, why this has not been a problem before. There must be some reason why it was different before declarative configuration, but I can't remember.
**Trask Stalnaker** 41:05 Did it have a name before?
That's…
**GZ Gregor Zeitlinger** 41:11 Right, it did not have a name, and just by the order of adding things, you could just override the distro. Yeah, that's the difference.
**Trask Stalnaker** 41:19 Yeah.
Yeah.
**GZ Gregor Zeitlinger** 41:22 Yeah, I think you have a good point.
**Trask Stalnaker** 41:28 What is, let's see, what is our distribution…
Maybe I can see it in the test, distro… Name, you know…
**GZ Gregor Zeitlinger** 41:50 the one.
It still feels odd that the user would have to say which distribution they are using.
It just is a possibility to shoot yourself into the foot to… for no apparent reason.
**Trask Stalnaker** 42:11 Well, they wouldn't, because you're automatically… Registering it… for them.
I think it's more for distros built on top of the Java agent.
that would… want to… Right.
that that would be important. Yeah, I don't think users would ever…
Really be exposed to that name.
Do we think… This is, already what we're publishing. I kind of wonder if this is…
And we might need to wait to change this.
till…
**Robert Niedziela** 42:55 I don't know.
**Trask Stalnaker** 42:56 Would want to do it in a major version, java agent…
**GZ Gregor Zeitlinger** 43:06 But what is that gaining?
**Trask Stalnaker** 43:09 I mean, it can't… isn't the Spring Boot starter a distro?
**GZ Gregor Zeitlinger** 43:15 It is.
**Trask Stalnaker** 43:17 Yeah, so… this… what does this mean? Does this mean the Java agent, or the Spring Boot Starter, or…
**GZ Gregor Zeitlinger** 43:26 This is the Java agent.
Just the Java agent.
**Trask Stalnaker** 43:31 Okay.
Yeah.
I mean, but that's not clear to me. Like, that is the repo?
To me.
**GZ Gregor Zeitlinger** 43:39 Okay.
**Trask Stalnaker** 43:48 Probably… We should… let me open an issue,
And tag it with Rio, because that would be, I think.
**GZ Gregor Zeitlinger** 44:02 We are free to change it now, because users are only using declarative configuration as a deliberate…
choice. They are not getting that for doing nothing.
**Trask Stalnaker** 44:19 Right, but in our vanilla non-declarative, don't we publish telemetry distro name resource attribute?
**GZ Gregor Zeitlinger** 44:31 Right, but we are free to do something different in declarative configuration, if we want to.
**Trask Stalnaker** 44:39 I see. We would need to… change… We'd need to conditionally Yeah.
conditionally emit…
**GZ Gregor Zeitlinger** 44:57 It's not conditionally. This, detector, is only used in declarative configuration. Without it, it does not take that code path.
**Trask Stalnaker** 45:06 there's two different names here, Gregor. One is the name of the…
provider itself.
And one is the attribute value.
That we emit.
for telemetry.distro.name, and they're… they're different, or they could be different. Although I think it would make sense for them to be the same value.
**GZ Gregor Zeitlinger** 45:42 But we are free to change both as we want in declarative configuration without
Changing what, happens without declarative configuration.
**Trask Stalnaker** 45:54 Okay.
Cool, I will just comment then. I think this…
I mean, that's what our jar is called.
Let's…
Go… Where did I…
Let's go with that.
**GZ Gregor Zeitlinger** 46:23 I'm thinking I'll split this up into two PRs, because all of the discussion now is about
The distribution part.
**Trask Stalnaker** 46:35 Sure. Yeah, let's, let's circle back here almost at the end of the PR, and then we'll look at the comments, and, I'm…
We should be okay to merge.
And… follow up.
Okay, okay, this is… okay, yes.
Okay, that's the assertions, yes, yes.
Okay, awesome. So let's… Look at what… Comments… were…
So that can… Yotsu… Okay…
I mean…
Okay.
The only one that, Like, it would…
be better to do immediately? Like, if all these other ones we can change, and nobody will notice.
If we dis… if we include service here… And then we remove it… That would affect… people.
**GZ Gregor Zeitlinger** 48:12 Yeah, I agree. I would also pull that to the later PR, so that we can discuss the service topic,
Separately.
**Trask Stalnaker** 48:21 Okay, so are you… so are you okay removing service from this PR, and then we'll discuss adding it later?
**GZ Gregor Zeitlinger** 48:31 Yeah, yeah, that's fine, sure.
**Trask Stalnaker** 48:33 Okay.
**GZ Gregor Zeitlinger** 48:34 And I should leave distribution, for now? Yeah.
**Trask Stalnaker** 48:39 Yeah.
**GZ Gregor Zeitlinger** 48:39 Fantastic. Okay.
**Trask Stalnaker** 48:40 Yeah.
So I will leave a comment saying that, and an approval…
C…
just… to that comment…
Okay.
Great.
I think we did it.
**GZ Gregor Zeitlinger** 50:02 Yep.
Thanks a lot!
**Trask Stalnaker** 50:05 Yup, see you in 10.
**GZ Gregor Zeitlinger** 50:08 So your intent?
**Robert Niedziela** 50:10 See ya, bye.
