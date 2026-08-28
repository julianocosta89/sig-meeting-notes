SIG: Injector SIG
Date: 2026-08-27
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana / OpenTelemetry** 01:25 Hey, Bastian.
**Bastian Krol (Dash0 Inc.)** 01:29 Hey Nikola, how are you?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:31 Oh, good, good.
**Bastian Krol (Dash0 Inc.)** 01:34 Yeah, medium, a little sick last few days, so… Slowly getting better.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:41 It seems it's, like, all over the world, I guess. I was sick yesterday or the day before.
**Bastian Krol (Dash0 Inc.)** 01:45 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:46 Not a lot, just a… just a little bit. Kind of headache, a little bit… So, I don't feel 100%, yeah.
**Bastian Krol (Dash0 Inc.)** 01:53 Yeah, yeah, I see, I see.
Yeah, it was kinda, kinda all out. I really felt super exhausted. Oh, this is mostly fine again.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:49 Have you implemented Ruby?
And the operator?
**Bastian Krol (Dash0 Inc.)** 02:54 Oh, that's yours.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:54 Or not yet?
**Bastian Krol (Dash0 Inc.)** 02:56 So, we have. I personally did not do that, but yeah, we included that. It's… been included in the latest operator versions. I think Matt Ware did that?
contributed set, so… Somewhat recently hired.
It's been around in several hotels.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:15 Oh, it's a really special.
**Bastian Krol (Dash0 Inc.)** 03:17 for a while.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:18 Hmm. Did you have to do any sort of… Like, sanity checking, do you remember? Do you know?
Like, we had to do for Python.
**Bastian Krol (Dash0 Inc.)** 03:26 I don't know. I… don't know from the top of my head. I can't take a quick look if I… Find something… Nikola Grcevski @ Grafana / OpenTelemetry 03:36 I don't know if Ruby's… same like Python, or similar to Node, or… I should research it.
**Bastian Krol (Dash0 Inc.)** 04:04 But I'm pretty sure it is probably an issue with different Ruby runtime versions, I guess? I… And there's also… but there doesn't seem to be extensive Checking going on… it looks like we… Just have a… scripture that just installs the Ruby… Nikola Grcevski @ Grafana / OpenTelemetry 04:30 realistic.
**Bastian Krol (Dash0 Inc.)** 04:30 Depends in the container, and… and that's that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:34 Third time.
**Bastian Krol (Dash0 Inc.)** 04:37 But I haven't been involved, so I… Nikola Grcevski @ Grafana / OpenTelemetry 04:39 You don't know.
Because I don't think all versions of Rails are supported as well, I was just… I sort of vaguely remember some customer wanting to use… OB data instead of Ruby SDK, because they were an old version of Rails or something, I don't know, so…
**Bastian Krol (Dash0 Inc.)** 04:56 Yeah, and I think it's also… isn't that… also similar, where Python, you have different Python distributions, you know, I think that's also a thing in Ruby, though I… Nikola Grcevski @ Grafana / OpenTelemetry 05:08 Alright, let's Yeah.
**Bastian Krol (Dash0 Inc.)** 05:10 Ruby and.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:11 Yeah, yeah. Some others.
**Bastian Krol (Dash0 Inc.)** 05:12 stuff that… Nikola Grcevski @ Grafana / OpenTelemetry 05:13 Yeah.
**Bastian Krol (Dash0 Inc.)** 05:14 But… the last line of Ruby I wrote probably 20 years ago.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:18 That's all, I mean…
**Bastian Krol (Dash0 Inc.)** 05:19 I really don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:22 No, I need to… I need to look into that.
**Bastian Krol (Dash0 Inc.)** 05:28 Hey, Antoine.
**Antoine Toulme (Splunk Inc.)** 05:29 Hey, I missed the first meeting, but I'm here for Injector.
**Bastian Krol (Dash0 Inc.)** 05:35 You didn't miss anything yet, but I get it, I mean, it's 5 minutes past, we can probably get started, not sure if anything… anyone else will show up.
**Antoine Toulme (Splunk Inc.)** 05:47 Yeah, no, don't have much time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:49 Jack's not here, I think he's traveling. He's in Europe right now, I think he's in Paris or something, yeah.
**Bastian Krol (Dash0 Inc.)** 05:56 I think Nikola also said that he's out for.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:57 He's away, yeah.
**Bastian Krol (Dash0 Inc.)** 05:58 If I remember correctly, so, it's probably all of us anyway.
The only thing on the agenda is the, is the, moving… Jacob to Amoritius.
PR, I feel like we already kind of agreed on something, so Antoine, your response there. I'm fine with keeping them on.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:25 Germany.
**Bastian Krol (Dash0 Inc.)** 06:26 Yeah, it's just… I also just write something, then we close it, discuss and SIG meeting.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:35 Yeah, he seems to be wanna… he seems to wanna continue.
Yep. And he closed the issue himself.
**Bastian Krol (Dash0 Inc.)** 06:42 Yep, yep.
**Antoine Toulme (Splunk Inc.)** 06:43 Yeah, no, Jacob's circumstances is that he's, he's very busy, he's been between two, three different jobs in the last few years.
But he's been working on the operator a lot as well.
And, huh.
You know, we're lucky to have him, not…
**Bastian Krol (Dash0 Inc.)** 07:00 Yeah.
**Antoine Toulme (Splunk Inc.)** 07:02 We need.
**Bastian Krol (Dash0 Inc.)** 07:03 Even if it…
**Antoine Toulme (Splunk Inc.)** 07:03 Yeah.
**Bastian Krol (Dash0 Inc.)** 07:04 Even if he wasn't super active on the Injector, having someone that is engaged with the operator is also super valuable for us, obviously, so… Yeah.
**Antoine Toulme (Splunk Inc.)** 07:16 Yeah, that's the thing, too, is like, even if he's not that active, I like having more people who are around, because when it comes time to have, like, maybe a heavy discussion, or a vote, or there's contention.
It's good to have people who are kind of able to kind of be, like, less nudgy, be kind of easy to go with, and… can help, like, build better consensus for SIGs, so… I think it can be used that way. Otherwise, it can be, very much like, three of us.
Until the end of times? Like, what are we doing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:51 Yeah, and maybe, like, I mean, it's a low-velocity project at this point, so… Yeah. I mean, there's no much chance for him to…
**Antoine Toulme (Splunk Inc.)** 08:00 It's a massive success.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:02 I agree, I agree.
I agree.
**Antoine Toulme (Splunk Inc.)** 08:05 Good. Like, one and done. Yeah, we can discuss more, like, additional things, but frankly, keeping it low drama and keeping releasing every often, but we're super happy with this, and… Now, we need to work on the operator.
And, that's it.
So…
**Bastian Krol (Dash0 Inc.)** 08:28 Yep, sounds good to me.
Do we have anything else?
**Antoine Toulme (Splunk Inc.)** 08:38 No, I think we were able to kind of get where we wanted with having the, injector work for our own use cases, which are still a little custom.
We will prob… I think we did move to that?
We've been using this old C code for a while, and it's just actually been very difficult to rip it out from our own.
Collector distribution, because it's been so, like, ingrained in our stuff.
I think we move to the Injector, or if we haven't, we should be.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:11 I mean, we're used to be Grafana.
Don't have a product officially released yet, but…
**Antoine Toulme (Splunk Inc.)** 09:19 That's pretty cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:20 Sometime.
**Antoine Toulme (Splunk Inc.)** 09:22 Yeah, more people in producing it, but better.
**Bastian Krol (Dash0 Inc.)** 09:25 Yeah, that'd be super valuable. The more exposure it gets.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:30 Huh.
**Bastian Krol (Dash0 Inc.)** 09:30 Edge cases we find. Absolutely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:33 Yep,
**Antoine Toulme (Splunk Inc.)** 09:36 Maybe we talk Windows next time?
In the coming months?
Quarter?
**Bastian Krol (Dash0 Inc.)** 09:44 Maybe not?
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:45 Maybe not.
**Antoine Toulme (Splunk Inc.)** 09:48 Let's try people. I mean… Nikola Grcevski @ Grafana / OpenTelemetry 09:49 I don't know if you saw, Antoine, but IBM released this new chip that supposedly runs both ARM ZOS instruction set, so…
**Antoine Toulme (Splunk Inc.)** 09:58 Yeah.
Oh, man.
**Bastian Krol (Dash0 Inc.)** 10:01 Okay, wild.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:02 So, like…
**Antoine Toulme (Splunk Inc.)** 10:04 Oh, shit.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:04 If you were… yeah.
390 on ARM, yeah.
**Antoine Toulme (Splunk Inc.)** 10:10 Alright, so, so, do you wanna… maybe you do want to have an update on that today?
The novella of, dealing with, legal, So after months of pushing around the CNCF legal, they came back and said, actually, we thought really hard about this, and we think that the maintainers should be able to sign the IBM agreement directly.
Teresa replied, we initiated the request towards you, because we don't want to sign this agreement, because the people running the GitHub Action Runners Are you the Linux Foundation?
So what the f- what are you talking about?
I was like, oh, that's a good point, let me put that into the discussion with the lawyers. That was 2 weeks ago.
Then I told them last week, I was like, this isn't acceptable. Like, what are you doing? This is bordering on incompetence. And the guy replied was like, well, actually, I'm traveling for a while, so I'm gonna put more people in the chat, and they can help.
And those people came and said, we like, we like legal discussions. And I go… And now what?
So… I don't know what I'm… I know what to do. I'm just pushing. The GC should actually, my boss is in the chat, Morgan, he's a member of the GC.
And, I've just started to nudge him and say, I think you need to report back to the GC that, you know, maybe the GC is going to have to make… to go sign this.
That, you know, the signature of a GC member on a piece of paper with IBM.
is not exactly engaging the OpenTeetry project.
Right?
The, the terms of use are… Like, you will agree that, you know, whatever is on the runners is… just… can be removed at any time, you're responsible for what runs on those things.
You have, like, some good… like, none of that is particularly… Dad?
There isn't anything about, like, IBM reusing your data for deferious purposes, there's… it's all just open source stuff, like, here's the thing.
We're good.
**Bastian Krol (Dash0 Inc.)** 12:21 Is it just to get CI runners? I'm missing the context. Okay, okay. That shouldn't be so hard.
**Antoine Toulme (Splunk Inc.)** 12:30 No.
The context behind this is that if you go to IBM Cloud, you used to be able to also, in IBM Cloud, just like AWS, provision VMs, right?
And you can provision VMs on X hardware, and you could provision VMs on IBM Z.
And recently, they stopped making that available as of February of this year.
And so the question is like, why did you do that?
how do we do this now? And they go, oh, you have to go through this program on the back. Like, it's no longer publicly available, you have to kind of… Go talk to the bouncer in the back of the building, and they'll let you in the other way.
And I think that open source program is the only way we're going to be able to get runners. Like, it's not like I can just get my credit card out and go, I, you know… I'm just gonna sponsor these for the project for next year.
It has to be done through… People are.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:27 Hey, Antoine, I actually have a suggestion, but maybe you won't like it. How about we just use QEMU to actually run it?
**Antoine Toulme (Splunk Inc.)** 13:35 I don't mind that much, it's better than nothing, but the… we brought this up before, and Nikele was like, no, that's good enough.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:43 Well, it's gonna be faster than the 390 that we're gonna get.
I mean, that's gonna be shared probably with a million people, and it's gonna be super slow.
**Antoine Toulme (Splunk Inc.)** 13:52 Oh, it's not about slow or fast, he was like, this is not close enough.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:55 It's not the real hardware?
**Antoine Toulme (Splunk Inc.)** 13:57 I want the wa- the waffles to smell, like, I want the nostrils to fill up with the smell of the burnt sepia.
**Bastian Krol (Dash0 Inc.)** 14:03 Is that, is that really realistic, a realistic concern that sounds like… Nikola Grcevski @ Grafana / OpenTelemetry 14:09 I mean… I mean, if Linux 390 can run on top of the emulator, I… I don't think LD preload and OTEL SDKs with some Java applications are the issue. If you can boot the kernel on it, You know, that's a real 390 kernel running, like, with all the bells and whistles.
I think that does so many more things to the actual underlying chip that's emulated than we will ever be able to do at the user space.
**Bastian Krol (Dash0 Inc.)** 14:37 Yeah, I think you have a very good point.
**I'm not a super big fan of Kimu, but… but in phase of… This alternative that sounds like, Nikola Grcevski @ Grafana / OpenTelemetry** 14:50 Yeah.
**Bastian Krol (Dash0 Inc.)** 14:50 Order of magnitude better.
And…
**Antoine Toulme (Splunk Inc.)** 14:54 But nothing.
**Bastian Krol (Dash0 Inc.)** 14:55 We can, I mean, we can make that kind of democratic decision if the three of us are in favor, and Nikhail is… Nikola Grcevski @ Grafana / OpenTelemetry 15:03 I mean, it gets me moving, and then if we ever wanted to order certify for 390 with… when we get the real hardware, we can run there, but at least now we can actually have a build, and maybe we can market experimental, if we're worried about, oh, we never tested this on real 390, because we don't have access to And maybe IBM can test it for us.
Cheers.
**Bastian Krol (Dash0 Inc.)** 15:24 I mean, who wins when we get it certified online, but that's not something that I'm particularly interested in. If it works, it works. And I guess for some big vendors that deal with IBM customers, it might be a thing, but… I don't care about that much.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:46 Yep.
**Antoine Toulme (Splunk Inc.)** 15:47 Yeah, no.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:47 Oh, yeah.
**Antoine Toulme (Splunk Inc.)** 15:48 more with you here, but there's been a drive, Nikola to move towards being very serious about those things. Actually, you gave me crap about the tier support systems that we have for the collector, where You know, we have Tier 3, Tier 2, Tier 1, and we have a lot of stuff that is stuck in Tier 3, where it's like, we build for it? Like, we cross-compile? And that's it. Like, that's all you get, right?
I think that's…
**Bastian Krol (Dash0 Inc.)** 16:11 Fair. That's, that's… but that's not what we're talking about here.
**Antoine Toulme (Splunk Inc.)** 16:14 Yeah, but he's conflating a little bit those two things.
**Bastian Krol (Dash0 Inc.)** 16:18 Yeah, that's my… I agree.
**Antoine Toulme (Splunk Inc.)** 16:21 yeah, that's what it is, you know. We can strive for perfection, but we also just be… I think having… things that are not done is a great driver to include more people into our community, too. Because the problem is that when you strive for perfection in doing things right, you're telling people, we don't really need you, we got it, right? And I like leaving stuff half-baked all the time, because then someone can come and feel like they are helping.
So, this is, this is open source. You have to… You have to give people, like, a bunch of angles that they can attach to your thing, right, and make it theirs.
**Bastian Krol (Dash0 Inc.)** 16:58 But that does not really apply to red tape and legal matters, like in this case. I mean.
**Antoine Toulme (Splunk Inc.)** 17:05 Indeed.
**Bastian Krol (Dash0 Inc.)** 17:05 We want a team of lawyers to be on this call every week.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:11 Yeah.
**Antoine Toulme (Splunk Inc.)** 17:11 No.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:13 I mean, I'll tell you, in the OB project, we ran ARM on ChemU for such a long time.
And until GitHub gave us… from Linux runners, and now we switched to them, but… Nobody ever had an arm issue.
**Antoine Toulme (Splunk Inc.)** 17:28 That's a bigger deal, I think, for EBPF, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:30 Yeah, I mean, we can't test on every possible ARM Linux kernel version, because the runners are only certain Linux kernel versions, and they keep moving, so we want to keep backwards compatibility I mean, in my opinion, if the OS boots.
Yeah, and EBPF is even lower level.
But…
**Antoine Toulme (Splunk Inc.)** 17:53 Thank you for that.
So, the OpenTelemetry Network project still has this, I think, is that we would run a virtual box, so we'd run the biggest runner you can get on GitHub Actions, which would be the Windows runner.
On which you would run the VirtualBox on it. The VirtualBox would then run the actual operating system of each of the Linux versions we wanted to certify on.
And then we would start the testing. And it was black box level testing. It's just, like, making sure the kernel hooks work, right? And they would test all manners of different versions of kernels on those things.
And it was pretty hilarious, because, you know, it kept blowing up in our faces. It was just not working.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:34 Yeah.
**Antoine Toulme (Splunk Inc.)** 18:35 It's just not meant to work.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:36 Yeah.
**Antoine Toulme (Splunk Inc.)** 18:37 So… that's an option, just like the nuclear option. It's like, you don't come back from this. Now you're, like, babysitting this build system every week.
Because the VirtualBox images disappear on you, things don't work, the thing, the way you think.
**You can't debug this… Nikola Grcevski @ Grafana / OpenTelemetry** 18:55 MU is, in my opinion, is… Bye.
**Antoine Toulme (Splunk Inc.)** 18:59 You'll.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:59 It's worked. Yeah.
**Antoine Toulme (Splunk Inc.)** 19:02 Yeah.
**Bastian Krol (Dash0 Inc.)** 19:03 We also used it, we also used it for quite a while to build your, multi… CPU arc images of the operator, and it was slow, but that was the only downside.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:17 And our tests are not really intensive in terms of CPU, so…
**Antoine Toulme (Splunk Inc.)** 19:22 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:23 When you asked about it on a platform, you said Windows, why not OpenBSD, or FreeBSD? I mean, they have the LD preload stuff.
**Antoine Toulme (Splunk Inc.)** 19:32 Boom.
Sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:33 run on that.
**Antoine Toulme (Splunk Inc.)** 19:35 What type of install… we don't really care, we just ship a .SO file, so they could install it on FreeBSD themselves, like, you can run Gen2, Whatever, right? Yeah, oh my gosh.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:48 Is it compatible?
**Antoine Toulme (Splunk Inc.)** 19:50 Wouldn't you not be? It's just a… Help, but… Nikola Grcevski @ Grafana / OpenTelemetry 19:55 I don't know, I don't think so, I think the…
**Antoine Toulme (Splunk Inc.)** 19:57 Good luck.
**Bastian Krol (Dash0 Inc.)** 19:58 they have different syscodes, and does it even… is it ELF-based? I mean, we rely… we are completely tied to ELF.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:05 Yeah.
**Bastian Krol (Dash0 Inc.)** 20:06 No, it's… Nikola Grcevski @ Grafana / OpenTelemetry 20:07 It is ELF-based, but I just wonder if it's, compatible in terms of… I mean, we grab GetEv, so… I haven't tried it, but I… I don't know.
I think it's not… Linux self, I think it's directly transferable.
I don't think so, but…
**Bastian Krol (Dash0 Inc.)** 20:27 supposed to try, but I'm still not sure if you were serious or just messing with us with the Windows.
**Antoine Toulme (Splunk Inc.)** 20:36 Well, the Windows thing is almost like a completely different project, because the stuff that we are talking about in this project applies. It's just that the product outcome is the same, which is that you have something you install.
It installs everything that you care about, about the system, and it does something. Actually, in the back, what you would do is that you manipulate the Windows registry in some form of elevated privileges at install time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:59 Yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 21:00 Yeah, I agree with that. It would be valuable to have something like that on Windows. I think it's far less valuable than Windows and other server operating systems.
**But… Nikola Grcevski @ Grafana / OpenTelemetry** 21:13 I'm not people.
**Bastian Krol (Dash0 Inc.)** 21:13 Endless.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:14 net people use it.
**Bastian Krol (Dash0 Inc.)** 21:15 Yeah, exactly.
But it is a completely new codebase. I think it's sometimes something that we could think about long-term, and I was very much against it in… in… when… when people asked about it in much earlier phases of the Injector. Now we are… quite stable, so we could take on something new, but we don't have the people. I think that's the main concern. We don't…
**Antoine Toulme (Splunk Inc.)** 21:44 people.
Yeah.
**Bastian Krol (Dash0 Inc.)** 21:46 no one of us, as far as I know, has the expertise to pull it off, so that's… That's.
**Antoine Toulme (Splunk Inc.)** 21:52 Well, we do. We've built something at Splunk where it's part of our open source. We're not being secretive about it. But there's really just a couple avenues that you need to explore. One is IIS.
Because I actually used quite a bit by folks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:07 Yeah.
**Antoine Toulme (Splunk Inc.)** 22:08 And that's pretty easy to just plug in. The other one is anything.net. So I think maybe this should be an offshoot of the .NET project at .NET SDK Contrib community. It could be a contribon at first, or something like that. I just want to point out that this is a huge population of users, and they're even less Linux users are actually fairly good, like, they would be able to get the job done without the Injector, right? I'm fairly confident.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:33 Yeah, okay.
**Antoine Toulme (Splunk Inc.)** 22:34 Nothing works, but I'm still… I don't have to install Java, right? On Windows, we're talking thousands of machines with no, like, proper automation, nothing done right way.
The way we do the auto transplantation for ourselves on Windows is that we have an MSI, which then performs actions by changing the registry on our behalf, installing additional elements, and all that.
And this is probably where we would want to go, so it could be an offshoot of… Is there a long-term an offshoot of the packaging project, or an offshoot of the .NET SDK?
But… I know it sounds dirty, but… I think, there's a lot of future for Windows, support, especially, like, this type of, kind of workstations, right? Thinking, like, thousands of people lining up, like.
IRS workstations, right? Imagine workers in a big building, right?
So… This type of stuff's gonna… it's gonna pay off at some point.
No, yeah, do we care right now? No. It's okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:39 Yeah, I think I get your point now. I think… I would… A lot more important than maybe FreeBSD, but… FreeBSD would have been really just another build of what we have, probably, with small tweaks here and there, but… But I think your… the customers are probably more impacted on Windows than on FreeBSD.
**Antoine Toulme (Splunk Inc.)** 24:01 I had more requests for X support than FreeBSD support, if you can believe that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:06 Yeah.
Yeah.
**Antoine Toulme (Splunk Inc.)** 24:08 That's terrible. I hate it. There we are.
It's just… Oh, actually, we… do we have AIC support for the Injector? Do we compile for that ecosystem?
**That might be a lower hanging fruit than all the… Nikola Grcevski @ Grafana / OpenTelemetry** 24:23 Yeah.
**Antoine Toulme (Splunk Inc.)** 24:23 craziness.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:26 Hmm.
**Antoine Toulme (Splunk Inc.)** 24:27 Anyway, just, if I, we should not make, let's not do any changes with Formicilles back, because… I don't want the first meeting when he's back, he's like, what have you done?
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:39 Why did you do this?
**Antoine Toulme (Splunk Inc.)** 24:40 Yeah.
Let's be respectful of his vacation time, too.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:50 This was our chance. What are you talking about? He's gonna come back, he will not want us to do this.
**Bastian Krol (Dash0 Inc.)** 24:57 They can be pretty stubborn about things.
**Antoine Toulme (Splunk Inc.)** 25:03 Well, maybe it works for him. I don't know.
Hasn't worked for me in life, I'm telling you, especially since I got married.
So, okay.
Well, it's great talking to you all.
Something goes off-camera, which is maybe a good idea.
**Diego Hurtado (Dash0)** 25:28 You know, no, no, I am.
**Antoine Toulme (Splunk Inc.)** 25:31 Good, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:32 Oh yeah, so Rachel's gonna comment on that issue and close it for Jacob, and I think we're good.
And we're gonna… next… by next week, we'll have both Windows and FreeBSD, so it's all good.
**Bastian Krol (Dash0 Inc.)** 25:43 Sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:47 I just want to say I won't be here next week, and neither will Jack. I think we have a company-wide event, Grafana Fest, that's happening in Vienna.
**Bastian Krol (Dash0 Inc.)** 25:54 The fifth.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:56 That sounds good.
**Antoine Toulme (Splunk Inc.)** 25:58 I've been making fun of, the Tyler and, Alex button. They moved to Grafana this summer from Honeycomb.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:07 Yeah.
**Antoine Toulme (Splunk Inc.)** 26:08 And I was telling them, like.
Do you think you'll get receptions in the backwoods in East Berlin when, you know, you… you're having a little festive, like, no, that's not… that's not Grafana. That's… that's Oligon, you're missing. It's not the right companies.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:22 Sorry.
**Antoine Toulme (Splunk Inc.)** 26:23 I don't know where you're meeting, and please don't disclose, because… Nikola Grcevski @ Grafana / OpenTelemetry 26:26 Vienna, being Vienna, yeah.
Oh, that's Vienna, yeah, so…
**Antoine Toulme (Splunk Inc.)** 26:30 Vienna?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:31 Yeah.
**Antoine Toulme (Splunk Inc.)** 26:32 like a Dynatrace occupation thing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:34 Yeah, yeah, I don't know how they managed to find us all hotels and houses organized, because it's, like, 1,500 people,
**Antoine Toulme (Splunk Inc.)** 26:44 Whoa.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:45 Yeah. Alright.
Yeah, we're gonna occupy Vienna. That's what it's called. Occupy Vienna Project, yeah.
**Antoine Toulme (Splunk Inc.)** 26:54 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:55 Yeah.
**Bastian Krol (Dash0 Inc.)** 26:58 Ouch.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:59 That's a joke.
**Antoine Toulme (Splunk Inc.)** 27:03 We've had a couple, like, 5 years going, we've had a competitor of ours who would have a conference same time as ours.
Like, did they.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:13 Wow.
**Antoine Toulme (Splunk Inc.)** 27:13 So people would come to the same conference.
Yes, beautiful.
Anyway. Yeah. Don't do that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:23 Don't do that. No. Okay.
**Antoine Toulme (Splunk Inc.)** 27:25 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:26 See you guys in two weeks.
**Bastian Krol (Dash0 Inc.)** 27:28 Bye-bye. Bye.
**Diego Hurtado (Dash0)** 27:30 Right.
