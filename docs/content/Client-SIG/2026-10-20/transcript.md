SIG: Client SIG
Date: 2026-10-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Cleo Schneider** 03:07 How you doing, Martin?
**Martin Kuba** 03:09 I'm doing alright. It's Tuesday.
**Cleo Schneider** 03:12 Here we are. We made it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:15 AA.
**Hanson Ho** 03:19 Hello?
Hold on the dark…
**Vishwan aranha** 03:48 Jason, is that The Shining?
**Jason Plumb** 03:53 Yeah, I finally found the one I was looking for, which is this one.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:00 Yeah.
**Jason Plumb** 04:02 Like, it's a trade-off. You either get the carpet, or you get the twins.
**Vishwan aranha** 04:07 Looks cool.
**Hanson Ho** 04:09 Is it like a shining background pack that Zoom allows you to download or something?
**Jason Plumb** 04:14 It's one that I've been carefully curating for myself over the last 5 years, yeah.
It's got, like, 4 images in it.
**Hanson Ho** 04:22 Nice.
**Jason Plumb** 04:24 Huh.
**Martin Kuba** 04:26 You've got a Halloween theme going.
**Jason Plumb** 04:28 Exactly.
Except every day is Halloween.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:41 The Timberline Lodge is also here on Mount Hood, so I feel like there's the Portland inside joke.
aspect of it.
**Jason Plumb** 04:50 Yep.
**Martin Kuba** 04:51 Alright.
**Jason Plumb** 04:52 But, like, only some exterior shots, I think, or… I don't think they filmed all of them.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:56 outside, you know.
**Hanson Ho** 05:02 Alrighty, wait another minute.
Any additional topics other than… Semantic Convention stuff, feel free to put them in.
I guess?
We can wait for the sake of waiting, or we can start.
What do y'all think?
**Jason Plumb** 05:39 Let's start, we're 4 in.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:40 Of course.
**Hanson Ho** 05:41 Alright.
All right, someone's a couple topics about, the, Semantic Invention Registry. So the first one, if you want to talk about it?
**Martin Kuba** 05:52 Yeah, just a couple of quick things. So the first one… This came up… pick, as I was looking at the… so we have a… we have a new, a PR to add another namespace, which is the end user namespace, and it's bringing over the, the attribute group.
And, I was… so I was looking, like, are the browser… the browser namespace has this, like, if you look at this description here, this client, client underscores client-side browser names, name for the group, and the end user one just basically copied what it was in the core. In the core, it was… I think it was just a leftover from… from the definition… from the format V1 format.
So it's… it seems… if I understand correctly, the V2 format doesn't require attributes to be assigned to a group. It's only for, documentation, I guess, if you wanted to, or for convenience, like, if you wanted to group certain attributes and reuse them for… in different places, So, and we had… So, as I was reviewing the end-user PR, I was thinking, well, like, maybe we… we should just not have… even have a discussion about, like, what the names for the group should be, like, let's just drop the group for now.
But we do have, a policy.
Here, that is enforcing that all attributes should be part of a group.
So what I'm proposing here is that we drop that policy.
Unless anyone has a reason to keep it.
Yeah, and then… Not add the groups, the attribute groups.
So I actually already opened a PR for this, At the bottom, at the bottom, and sort of if you want to click on that, so… the details… On that, it's… it's… so if you look at the files, files changed?
So it's… it's dropping the policy, and it's also, as a result, it's gonna drop the… the attribute groups, markdown file in Docs.
But that's all. So…
**Hanson Ho** 08:28 Yeah, so the, the policy was put in because the assumption was that, everything's gonna be V2, and, the groups are gonna be, basically.
how folks consume dependencies, from… from this version, or from this registry. So they'll say, for version 1.5, I depend on this group, and that will pull in a bunch of attributes instead of, like, a single.
attributes. It's just easier to manage. But if we're not uniformly saying that every attribute Should… or if we're not formally saying that, every dependency we're exporting, should be via a group, and consumption be a group, and we allow for individual attributes to be, consumed, then we should probably drop this policy until that is more enforced. From my reading, that was what V2 was supposed to be like, but I guess things aren't fully on board for V2, and there's no use to be… being that strict if If the consumption, isn't… isn't even that strict, so… I'm okay with reversing this. What do y'all think?
**Jason Plumb** 09:48 How do the policies apply to this? So does it still allow for groups to be used in the future?
**Hanson Ho** 09:54 Yes, so the initial policy right now was, the idea is that if the public interface is, the group.
And if you have an attribute that is effectively public, but not in the part of a group, it's… nobody can consume it. But if that's no longer… that's not true, that you can still consume without the group, you can still consume the individual attributes, then this is going a little bit overboard and saying… like, the idea is that oh, you don't have these attributes, just don't belong to groups that people are just depending on, you know, you know, ad hoc, one by one. But if we don't have that requirement anymore, then… and we allow for that individual attributes to be pulled, then this is, a bit, overboard. So you can still…
**Jason Plumb** 10:37 But this… just to be clear, like, this is a net relaxing of the requirement. It doesn't preclude groups from existing or from… those from being leveraged in the future.
**Martin Kuba** 10:47 Correct.
**Jason Plumb** 10:48 Cool, yeah, it sounds good, then, to me.
**Hanson Ho** 10:52 That was put in there for validation, and the premise is… is false, so we should remove the validation. For now, at least.
Cool, I'll take a look today and, probably prove it and get it merged.
Alright.
Second one.
**Martin Kuba** 11:12 Yeah, and the other one, this ties to what I was… Talking about last week, the steps for migrating the namespaces from core to here, I went to the cement to the semantic convention SIG yesterday, just to run this by them.
And actually, I think the process can actually be simpler, so I updated… I updated the, the description here for the steps that can be taken. The gist of it is that, we don't have to wait for If you just wanna, like.
look at the description there, the steps. So, the gist of it is that we don't have to wait for the core to release.
To do a release, we can… we can just, as part of our… as part of merging our… the Migrate namespace, we just, We just point the manifest file to, like, a commit hash, instead, like, temporarily, and then when the core releases, then we'll change it back to the version.
**Hanson Ho** 12:18 And they're okay with us pointing to a hash.
**Martin Kuba** 12:20 Yes, yes.
**Hanson Ho** 12:21 Okay, alright, sounds good. Whatever objections I have, doesn't matter.
**Martin Kuba** 12:28 And so we can, we have the end space, sorry, end space, end user.
PR Open, so we can… we can take that as the first… First test, test run.
**Hanson Ho** 12:42 Cool. Does that mean that folks can also point to one of our hashes and say, that's what we depend on?
**Martin Kuba** 12:50 Yeah.
**Hanson Ho** 12:51 All right. So releases are just nice, kind of, milestones that we can say, hey, these are what's included, and these are what's changed from the previous one.
Interesting, and that's… is that how the other registries are getting away with release… not releasing, is just pointing to hashes?
**Martin Kuba** 13:11 Good question. I haven't looked at that.
**Hanson Ho** 13:15 Okay, yeah, I'm fine with it, especially since we haven't officially declared a release anyway, but… I, or, or, or every, every commit is a release, I don't know what is true.
All right, sounds good. Anybody object to this?
YOLO!
Hashes are released now.
**Martin Kuba** 13:41 I mean, I'm not… to be clear, I'm not saying that we should have… be pointing to a hash, like, we should be pointing to, like, a released version, but… This shouldn't stop us from, you know, from migrating, so…
**Hanson Ho** 13:55 Yeah, we have… should have Renovate set up, so when they do release a new one, we can probably… when… as part of the, the process to… to basically, upgrade, Actually, how would that work?
If we're depending on a hash and not a release, is Renovate gonna pick that up? I'm gonna have to test that.
Okay.
Anyway, this, this is fine.
Cool?
Any other topics? I didn't do a release last week, because I ran out of time, but I think after, well… makes it less… less necessary to do a release, after this, but I think we should still do it, just in case, but it also means that it's less… If the release is screwed up, it doesn't really matter.
So, yeah, it makes it less useful, but less… downsides. So, anyway.
**Jason Plumb** 14:57 I think getting that process started kind of early and making it repeatable is… like, that's where the real value is right now. What… Are there artifacts? Like, what does the release do?
**Hanson Ho** 15:11 So, the release… so I think it should be in the README, or the releases markdown, but basically, it just creates, a version, that, that… that says… that… well, right now it only does dev releases, so we are not… we don't have a stable line and a dev line, but eventually we'll have a stable line and a dev line. Dev will include everything, stable will include, everything that is, not experiment, or whatever… whatever the… the marker is.
And it'll… it'll basically publish a GitHub, release. The URL will be pinned, to some tag, that is immutable. I think we turned it on, but, you know.
**Jason Plumb** 15:55 Oh, cool, okay.
Yeah, so is that something that is set, like, through the, Terraform stuff?
**Hanson Ho** 16:07 Probably, because I didn't manually do it.
It must be.
**Jason Plumb** 16:11 It seems like… it seems very helpful to have immutable tags for this stuff.
**Hanson Ho** 16:17 Yeah, I think the doc describes the, tags should be immutable by convention, but I think, the WIPO was set up such that they are immutable. Cool.
Or, yeah, yeah.
We can double-check that, but… But it should allow us to say we have a version in the dev that means certain things. Folks can track… trace back and put in their schema and all that fun stuff, so… Alright.
Anything else y'all want to talk about?
I guess there's a bunch of browser conventions already, and the other ones are being slowly migrated.
Yeah, we'll just, I guess.
all those conventions in this, in this registry and deal with them, as we would.
**Jason Plumb** 17:15 I'm excited to see how it looks for Android and how we can start leveraging it.
**Hanson Ho** 17:20 It'll look very similar, except it'll just be pulling from a different source, like, the PR has been… well. Yeah.
**Jason Plumb** 17:27 In school.
**Hanson Ho** 17:30 Awesome.
Anything else, so we can get our 15 minutes back?
**Jason Plumb** 17:36 Ted, do you have anything for us?
Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:40 Nope.
**Jason Plumb** 17:41 Cool.
**Hanson Ho** 17:42 Alrighty.
Talk to you folks later.
**Martin Kuba** 17:47 See you later. Thanks.
**Jason Plumb** 17:48 here.
